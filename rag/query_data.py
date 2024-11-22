import os
import argparse
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are a helpful assistant. Answer the user's question using only the context provided below.

Context:
{context}

Question:
{question}

Answer:
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    parser.add_argument(
        "--k", type=int, default=1, help="Number of contexts to retrieve from the database (default: 1)"
    )
    args = parser.parse_args()
    query_text = args.query_text
    k = args.k

    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_relevance_scores(query_text, k=k)
    if not results:
        print(f"Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print("Prompt generated for the query:")
    print(prompt)

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

        generated_text = completion.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error calling the inference API: {e}")
        return

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    sources = [src for src in sources if src]  
    new_sources = []

    for src in sources:
        if src not in new_sources:
            new_sources.append(src)
    
    formatted_response = f"Response: {generated_text}\nSources: {new_sources if new_sources else 'No sources found.'}"
    print(formatted_response)

if __name__ == "__main__":
    main()
