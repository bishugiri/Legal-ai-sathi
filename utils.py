from langchain_community.document_loaders import PyPDFLoader
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ConstitutionVectorStore:
    def __init__(self):
        self.model = None
        self.documents = []
        self.paragraphs = []
        
    def load_and_process_document(self, pdf_path):
        """Load and process a PDF document"""
        # Load PDF
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        
        # Split text into paragraphs
        paragraphs = []
        for page in pages:
            # Split by newlines to get paragraphs
            page_paragraphs = page.page_content.split('\n\n')
            paragraphs.extend([p.strip() for p in page_paragraphs if p.strip()])
        
        # Preprocess paragraphs
        processed_paragraphs = [simple_preprocess(p) for p in paragraphs]
        
        # Create tagged documents
        tagged_data = [TaggedDocument(words=words, tags=[str(i)]) 
                      for i, words in enumerate(processed_paragraphs)]
        
        # Train Doc2Vec model
        self.model = Doc2Vec(vector_size=100, min_count=2, epochs=40)
        self.model.build_vocab(tagged_data)
        self.model.train(tagged_data, total_examples=self.model.corpus_count, 
                        epochs=self.model.epochs)
        
        # Store original paragraphs
        self.paragraphs = paragraphs
        self.documents = paragraphs
        
        return self
    
    def similarity_search(self, query, k=1):
        """Find most similar paragraphs to the query"""
        # Preprocess query
        query_words = simple_preprocess(query)
        
        # Get query vector
        query_vector = self.model.infer_vector(query_words)
        
        # Get document vectors
        doc_vectors = [self.model.dv[str(i)] for i in range(len(self.paragraphs))]
        
        # Calculate similarities
        similarities = cosine_similarity([query_vector], doc_vectors)[0]
        
        # Get top k most similar paragraphs
        top_k_indices = np.argsort(similarities)[-k:][::-1]
        
        # Return paragraphs and their similarities
        results = []
        for idx in top_k_indices:
            results.append({
                'content': self.paragraphs[idx],
                'similarity': float(similarities[idx])
            })
        
        return results

def create_vector_store(pdf_path):
    """Create a vector store from PDF"""
    vector_store = ConstitutionVectorStore()
    return vector_store.load_and_process_document(pdf_path)

def get_vector_store():
    """Get existing vector store"""
    # Since we're using an in-memory store, we need to recreate it each time
    return None

def create_chat_chain(vector_store):
    """Create a chat chain with the vector store"""
    return vector_store

def get_response(chain, query):
    """Get response from the chain"""
    # Get similar paragraphs
    results = chain.similarity_search(query, k=3)
    
    # Format the response
    answer = "\n\n".join([result['content'] for result in results])
    sources = [result['content'] for result in results]
    
    return {
        "answer": answer,
        "sources": sources
    } 