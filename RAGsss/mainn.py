import os
from RAGsss.vector_embeddings import *
from RAGsss.RAG_Query_With_Buffer import *


# Define paths
PDF_DIR = os.getenv("PDF_DIR", "./pdfs/")
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "./ChromaDB_VectorStore/")

# Load and embed documents
logger.info("Loading and embedding documents...")
chunks = []
for pdf_file in os.listdir(PDF_DIR):
    try:
        pages = load_file(os.path.join(PDF_DIR, pdf_file))
        chunks += split_doc(pages)
    except Exception as e:
        logger.error(f"Error loading {pdf_file}: {e}")

vectorDB = embedd_chunks(chunks, VECTOR_STORE_PATH)

# Load vector store and set up QA chain
vectorDB = saved_vectorDB_loading(VECTOR_STORE_PATH)
qa_prompt_template = QA_context_prompting()
qa_memory = QA_with_memory(llm=None, vectorDB=vectorDB, qa_prompt_template=qa_prompt_template)

# Query the system
while True:
    question = input("Enter your question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        break
    response = get_response(question, qa_memory)
    print(response)
