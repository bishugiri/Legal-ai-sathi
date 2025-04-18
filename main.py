import streamlit as st
from utils.document_loader import load_and_process_document, create_vector_store, get_vector_store
from utils.chat_utils import create_chat_chain, get_response
import os

def initialize_vector_store():
    """Initialize or load the vector store"""
    vector_store = get_vector_store()
    if vector_store is None and os.path.exists("docs/nepal-constitution.pdf"):
        documents = load_and_process_document("docs/nepal-constitution.pdf")
        vector_store = create_vector_store(documents)
    return vector_store

def main():
    # Header with chatbot name and developer info
    st.markdown(
        """
        <div style='text-align: center; margin-bottom: 20px;'>
            <h1 style='color: #6A0DAD;'>Legal AI Saathi</h1>
            <p style='color: #666; font-size: 14px;'>Developed by Sankhya AI</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chain" not in st.session_state:
        st.session_state.chain = None
    
    # Sidebar for configuration
    with st.sidebar:
        st.markdown(
            """
            <style>
            .sidebar .sidebar-content {
                background-color: #6A0DAD;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<h2 style='color: white;'>Status</h2>", unsafe_allow_html=True)
        
        # Initialize vector store and chat chain
        vector_store = initialize_vector_store()
        if vector_store and st.session_state.chain is None:
            with st.spinner("Initializing Phi-2 model..."):
                st.session_state.chain = create_chat_chain(vector_store)
                st.success("System initialized successfully!")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            if "sources" in message:
                with st.expander("View Sources"):
                    for source in message["sources"]:
                        st.markdown(f"```\n{source}\n```")
    
    # Chat input
    if prompt := st.chat_input("What would you like to know about Nepal's constitution?"):
        if st.session_state.chain is None:
            st.error("System not initialized. Please check if the constitution document is loaded properly.")
            return
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                response = get_response(st.session_state.chain, prompt)
                st.write(response["answer"])
                if response["sources"]:
                    with st.expander("View Sources"):
                        for source in response["sources"]:
                            st.markdown(f"```\n{source}\n```")
        
        # Add assistant response to chat history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response["answer"],
            "sources": response["sources"]
        })

if __name__ == "__main__":
    main() 