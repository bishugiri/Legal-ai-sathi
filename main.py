import streamlit as st

def get_legal_response(prompt):
    responses = {
        "What are the basic rights under Nepal's constitution?": """
        The Constitution of Nepal 2072 guarantees several fundamental rights including:
        1. Right to Equality
        2. Right to Freedom
        3. Right to Justice
        4. Right to Education
        5. Right to Health
        6. Right to Employment
        7. Right to Property
        8. Right to Privacy
        9. Right to Information
        10. Right to Constitutional Remedy
        
        These rights are protected under Part 3 of the Constitution and can be enforced through the Supreme Court.
        """,
        
        "How to register a company in Nepal?": """
        Company registration in Nepal involves the following steps:
        1. Name Clearance from Office of Company Registrar
        2. Prepare Memorandum of Association (MOA) and Articles of Association (AOA)
        3. Submit documents to Company Registrar's Office
        4. Pay registration fees
        5. Obtain Company Registration Certificate
        6. Register for PAN and VAT
        7. Open a bank account
        
        Required documents include:
        - Citizenship certificate of promoters
        - PAN registration certificate
        - MOA and AOA
        - Board resolution
        - Office address proof
        """,
        
        "What is the process for property registration?": """
        Property registration in Nepal involves:
        1. Prepare required documents:
           - Land ownership certificate
           - Tax clearance certificate
           - Citizenship certificate
           - Survey map
        2. Submit application at Land Revenue Office
        3. Pay registration fees
        4. Get property registered in your name
        
        The process typically takes 15-30 days depending on the location and completeness of documents.
        """,
        
        "Explain the court system in Nepal": """
        Nepal's court system is structured as follows:
        1. Supreme Court (Highest Court)
        2. High Courts (7 in total)
        3. District Courts (77 in total)
        4. Specialized Courts:
           - Revenue Tribunal
           - Administrative Court
           - Labor Court
           - Debt Recovery Tribunal
        
        The Supreme Court is the highest court of appeal and has the power of judicial review.
        """,
        
        "What are the labor laws in Nepal?": """
        Key labor laws in Nepal include:
        1. Labor Act, 2074
        2. Social Security Act, 2075
        3. Trade Union Act, 2049
        
        Main provisions:
        - 8 hours work day
        - Minimum wage (currently NPR 17,300 per month)
        - Paid leave (annual, sick, maternity)
        - Social security benefits
        - Workplace safety requirements
        - Right to form trade unions
        """,
        
        "How to file a case in District Court?": """
        Steps to file a case in District Court:
        1. Prepare plaint/application with:
           - Names and addresses of parties
           - Facts of the case
           - Relief sought
           - Supporting documents
        2. Pay court fees
        3. Submit to District Court
        4. Get case number and hearing date
        5. Attend hearings
        6. Present evidence
        7. Get judgment
        
        Note: Legal representation is recommended but not mandatory.
        """,
        
        "What are the requirements for marriage registration?": """
        Requirements for marriage registration in Nepal:
        1. Both parties must be of legal age (20 years)
        2. Required documents:
           - Citizenship certificates
           - Age proof
           - Photos
           - Affidavit of single status
        3. Submit application at:
           - Local Ward Office
           - District Administration Office
        4. Pay registration fee
        5. Get marriage certificate
        
        Note: Foreign nationals need additional documents.
        """,
        
        "Explain the tax laws for businesses in Nepal": """
        Main business taxes in Nepal:
        1. Income Tax:
           - Corporate tax rate: 25%
           - Small business: 20%
        2. VAT:
           - Standard rate: 13%
           - Registration threshold: NPR 50 lakhs
        3. Excise Duty:
           - Varies by product
        4. Customs Duty:
           - Varies by import category
        
        Tax filing deadlines:
        - Income Tax: 3 months after fiscal year end
        - VAT: Monthly/Quarterly
        - TDS: Monthly
        """
    }
    return responses.get(prompt, f"Echo: {prompt}")

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
    
    # Sample prompts related to Nepal's legal sector
    sample_prompts = [
        "What are the basic rights under Nepal's constitution?",
        "How to register a company in Nepal?",
        "What is the process for property registration?",
        "Explain the court system in Nepal",
        "What are the labor laws in Nepal?",
        "How to file a case in District Court?",
        "What are the requirements for marriage registration?",
        "Explain the tax laws for businesses in Nepal"
    ]
    
    # Sidebar with sample prompts
    with st.sidebar:
        st.markdown(
            """
            <style>
            .sidebar .sidebar-content {
                background-color: #6A0DAD;
            }
            .stButton>button {
                color: white;
                background-color: #6A0DAD;
                border: none;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<h2 style='color: white;'>Sample Prompts</h2>", unsafe_allow_html=True)
        
        for prompt in sample_prompts:
            if st.button(prompt, key=f"prompt_{prompt}"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                response = get_legal_response(prompt)
                st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Generate and display assistant response
        response = get_legal_response(prompt)
        with st.chat_message("assistant"):
            st.write(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main() 