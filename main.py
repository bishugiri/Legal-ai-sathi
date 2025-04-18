import streamlit as st
from utils import create_vector_store, create_chat_chain, get_response
import os

def initialize_vector_store():
    """Initialize the vector store"""
    if os.path.exists("docs/nepal-constitution.pdf"):
        vector_store = create_vector_store("docs/nepal-constitution.pdf")
        return vector_store
    return None

def main():
    # Custom CSS for light gray background and better styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f5f5f5;
        }
        .chat-message {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            color: black;
        }
        .sample-prompt {
            cursor: pointer;
            padding: 10px;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 5px 0;
            color: black;
        }
        .sample-prompt:hover {
            background-color: #f0f0f0;
        }
        /* Ensure all text in the app is black */
        .stMarkdown, .stTextInput, .stButton, .stChatMessage {
            color: black !important;
        }
        /* Sidebar specific styling */
        .sidebar .stButton button {
            color: white !important;
        }
        .sidebar .stMarkdown {
            color: white !important;
        }
        /* Chat specific styling */
        .stChatMessage .stMarkdown {
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
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
    
    # Sidebar for configuration and sample prompts
    with st.sidebar:
        st.markdown(
            """
            <style>
            .sidebar .sidebar-content {
                background-color: #6A0DAD;
            }
            .sidebar .stButton button {
                color: white !important;
                margin-top: 0;
            }
            .sidebar .stMarkdown {
                color: white !important;
                margin-top: 0;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        # Sample prompts section at the very top
        st.markdown("<h3 style='color: white; margin-top: 0;'>Sample Questions</h3>", unsafe_allow_html=True)
        sample_prompts = [
            "What are the fundamental rights in Nepal's constitution?",
            "How is the President elected in Nepal?",
            "What is the process of amending the constitution?",
            "What are the rights of women according to the constitution?",
            "How is the judiciary system structured?",
            "What are the citizenship requirements?",
            "Explain the federal structure of Nepal",
            "What are the official languages of Nepal?"
        ]
        
        for prompt in sample_prompts:
            if st.button(prompt, key=prompt):
                st.session_state.current_prompt = prompt
        
        # Initialize vector store and chat chain
        vector_store = initialize_vector_store()
        if vector_store and st.session_state.chain is None:
            with st.spinner("Initializing model..."):
                st.session_state.chain = create_chat_chain(vector_store)
                st.success("System initialized successfully!")
    
    # Main chat area with light gray background
    chat_container = st.container()
    with chat_container:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(f"<div class='chat-message'>{message['content']}</div>", unsafe_allow_html=True)
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
            st.markdown(f"<div class='chat-message'>{prompt}</div>", unsafe_allow_html=True)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                response = get_response(st.session_state.chain, prompt)
                st.markdown(f"<div class='chat-message'>{response['answer']}</div>", unsafe_allow_html=True)
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