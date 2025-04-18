from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

def load_and_process_document(pdf_path):
    """
    Load and process a PDF document
    """
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    documents = text_splitter.split_documents(pages)
    
    return documents

def create_vector_store(documents):
    """
    Create a vector store from documents
    """
    # Use a smaller embeddings model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )
    
    # Create the vector store
    vector_store = FAISS.from_documents(documents, embeddings)
    
    # Save the vector store
    vector_store.save_local("vector_store")
    
    return vector_store

def get_vector_store():
    """
    Get existing vector store
    """
    if os.path.exists("vector_store"):
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        return FAISS.load_local("vector_store", embeddings)
    
    return None 