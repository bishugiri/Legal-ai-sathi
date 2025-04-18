from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_chat_chain(vector_store):
    """Create a chat chain with the vector store"""
    # Initialize the LLM
    model_name = "google/flan-t5-small"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=512,
        temperature=0.7
    )
    
    llm = HuggingFacePipeline(pipeline=pipe)
    
    # Create memory for conversation
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # Create the chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
        chain_type="stuff",
        return_source_documents=True
    )
    
    return chain

def get_response(chain, query):
    """Get response from the chain"""
    response = chain({"question": query})
    
    # Format the response
    answer = response["answer"]
    sources = [doc.page_content for doc in response["source_documents"]]
    
    return {
        "answer": answer,
        "sources": sources
    } 