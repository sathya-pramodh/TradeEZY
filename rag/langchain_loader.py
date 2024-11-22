import nltk
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
import shutil
from PyPDF2 import PdfReader

nltk.data.path.append('/home/amogh/nltk_data')
nltk.download('punkt')

CHROMA_PATH = "chroma"
DATA_PATH = "data/SEM"

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents():
    pdf_files = [f for f in os.listdir(DATA_PATH) if f.endswith('.pdf')]
    
    documents = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(DATA_PATH, pdf_file)
        
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        
        if text.strip():
            documents.append(Document(page_content=text, metadata={"source": pdf_file}))

    if not documents:
        raise ValueError(f"No documents found in {DATA_PATH}.")
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    if chunks:
        document = chunks[0]
        print("Example Chunk Content:")
        print(document.page_content)
        print("Metadata:")
        print(document.metadata)

    return chunks

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2") 

    db = Chroma.from_documents(
        chunks, embeddings, persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
