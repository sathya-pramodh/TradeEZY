import os
import json
import argparse
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma"
MEMORY_FILE = "memory.json"

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

# Function to load memory from a file
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save memory to a file
def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def main():
    # Load persistent memory
    memory = load_memory()

    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    parser.add_argument(
        "--k", type=int, default=1, help="Number of contexts to retrieve from the database (default: 1)"
    )
    args = parser.parse_args()
    query_text = args.query_text
    k = args.k

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
        return

    # Extract and deduplicate sources
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    sources = [src for src in sources if src]
    unique_sources = list(dict.fromkeys(sources))

    # Save the current interaction to memory
    memory.append({"user": query_text, "assistant": generated_text})
    save_memory(memory)  # Persist updated memory

    # Format and print the response
    formatted_response = f"Response: {generated_text}\nSources: {unique_sources if unique_sources else 'No sources found.'}"
    print(formatted_response)

if __name__ == "__main__":
    main()
