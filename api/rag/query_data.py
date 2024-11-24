import os
import argparse
from pymongo import MongoClient
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_PATH")

PROMPT_TEMPLATE = """
You are a helpful assistant. Answer the user's question using only the context provided below and the conversation history.

Context:
{context}

Conversation History:
{history}

Question:
{question}

Answer:
"""

# Function to load memory from MongoDB
def load_memory(user_id):
    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client.chatbot_db
    collection = db.memory
    memory_doc = collection.find_one({"user_id": user_id})
    if memory_doc and "memory" in memory_doc:
        return memory_doc["memory"]
    return []

# Function to save memory to MongoDB
def save_memory(user_id, memory):
    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client.chatbot_db
    collection = db.memory
    collection.update_one({"user_id": user_id}, {"$set": {"memory": memory}}, upsert=True)

def generate_answer(user_id, prompt, k=10):

    # Load persistent memory from MongoDB
    memory = load_memory(user_id)

    query_text = prompt

    # Prepare embeddings and Chroma database
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search for similar contexts
    results = db.similarity_search_with_relevance_scores(query_text, k=k)
    if not results:
        print(f"Unable to find matching results.")
        return

    # Combine context from search results
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    # Add conversation history to the prompt
    conversation_history = "\n".join([f"User: {entry['user']}\nAssistant: {entry['assistant']}" for entry in memory])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, history=conversation_history, question=query_text)
    print("Prompt generated for the query:")
    print(prompt)

    # Call the Hugging Face inference client
    client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API"))

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct",  
            messages=messages,
            max_tokens=300
        )

        # Extract generated text
        generated_text = completion.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error calling the inference API: {e}")
        return e

    # Extract and deduplicate sources
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    sources = [src for src in sources if src]
    unique_sources = list(dict.fromkeys(sources))

    # Save the current interaction to memory in MongoDB
    memory.append({"user": query_text, "assistant": generated_text})
    save_memory(user_id, memory)  # Persist updated memory

    # Format and print the response
    formatted_response = f"Response: {generated_text}\nSources: {unique_sources if unique_sources else 'No sources found.'}"
    print(formatted_response)
    return formatted_response

