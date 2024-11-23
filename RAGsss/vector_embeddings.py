import os
import logging
import torch
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load documents from a file
def load_file(path=None):
    if path is None:
        raise ValueError("Path must be provided.")

    logger.info("Loading Document...")
    loader = PyPDFLoader(path)
    pages = loader.load()
    return pages

# Split documents into chunks
def split_doc(pages, chunk_size: int = 1000, chunk_overlap: int = 4):
    if not pages:
        raise ValueError("The 'pages' list is empty. Provide valid document content.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(pages)

    if not chunks:
        raise ValueError("No chunks were created. Check the input data.")

    logger.info(f"Split {len(pages)} documents into {len(chunks)} chunks.")
    return chunks

# Embed chunks into vector database
def embedd_chunks(chunks, save_directory):
    if not chunks:
        raise ValueError("The 'chunks' argument cannot be empty.")
    if save_directory is None:
        raise ValueError("The 'save_directory' must be provided.")

    os.system(f"rm -rf {save_directory}")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"Using device: {device}")

    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs={'device': device}
    )

    vectorDB = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=save_directory
    )

    vectorDB.persist()
    logger.info(f"Saved {len(chunks)} chunks to {save_directory}.")
    return vectorDB

# Load vector store
def saved_vectorDB_loading(save_directory):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs={'device': device}
    )
    vectorDB = Chroma(persist_directory=save_directory, embedding_function=embeddings)
    return vectorDB
