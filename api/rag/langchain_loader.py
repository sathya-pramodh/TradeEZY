import nltk
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()

nltk_data_path = os.getenv("NLTK_DATA_PATH", './nltk_data')

if nltk_data_path and not os.path.exists(nltk_data_path):
    print(f"Warning: NLTK data path '{nltk_data_path}' does not exist. Creating it.")
    os.makedirs(nltk_data_path, exist_ok=True)

os.environ['NLTK_DATA'] = nltk_data_path

nltk.data.path.append(os.environ['NLTK_DATA'])

nltk.download('punkt')

CHROMA_PATH = "chroma"
DATA_PATH = os.path.join(os.path.dirname(__file__), os.getenv("DATA_PATH"))

def generate_data_store(uploaded_files=None):
    # Load documents from existing files and uploaded files
    existing_documents = load_documents_from_directory(DATA_PATH)
    uploaded_documents = load_documents_from_uploads(uploaded_files) if uploaded_files else []
    all_documents = existing_documents + uploaded_documents

    # Split text into chunks
    chunks = split_text(all_documents)

    # Save chunks to Chroma
    save_to_chroma(chunks)

def load_documents_from_directory(directory):
    documents = []
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        try:
            with open(pdf_path, 'rb') as f:
                reader = PdfReader(f)
                text = ""

                # Extract text from each page
                for page in reader.pages:
                    text += page.extract_text()

            # Add to documents if text is not empty
            if text.strip():
                documents.append(Document(page_content=text, metadata={"source": pdf_file}))
        except Exception as e:
            print(f"Error processing file {pdf_file}: {e}")
            continue

    return documents

def load_documents_from_uploads(uploaded_files):
    documents = []

    for file in uploaded_files:
        try:
            # Read the uploaded PDF file
            reader = PdfReader(file)
            text = ""

            # Extract text from each page
            for page in reader.pages:
                text += page.extract_text()

            # Add to documents if text is not empty
            if text.strip():
                documents.append(Document(page_content=text, metadata={"source": file.filename}))
        except Exception as e:
            print(f"Error processing file {file.filename}: {e}")
            continue

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
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

    if os.path.exists(CHROMA_PATH):
        # Load existing database and add new chunks
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
        db.add_documents(chunks)
        print(f"Updated Chroma database with {len(chunks)} new chunks.")
    else:
        # Create a new database
        db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
        print(f"Created a new Chroma database with {len(chunks)} chunks.")

    db.persist()
