# Legal AI Saathi

A chatbot that helps users understand the Nepal Constitution by answering questions about its contents.

## Features

- PDF document processing
- Vector-based semantic search
- Conversational interface
- Source citation for answers

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/legal-ai-saathi.git
cd legal-ai-saathi
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Hugging Face API key:
```
HUGGINGFACE_API_KEY=your_api_key_here
```

4. Place your PDF document in the `docs` directory

## Usage

Run the Streamlit app:
```bash
streamlit run main.py
```

The app will be available at `http://localhost:8501`

## Project Structure

```
legal-ai-saathi/
├── docs/                    # PDF documents
├── utils/                   # Utility functions
│   ├── chat_utils.py       # Chat-related functions
│   └── document_loader.py  # PDF processing functions
├── main.py                 # Main application
├── requirements.txt        # Dependencies
└── README.md              # Documentation
```

## Dependencies

- streamlit
- langchain
- langchain-community
- transformers
- sentence-transformers
- faiss-cpu
- pypdf
- python-dotenv

## License

MIT License 