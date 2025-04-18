# Legal AI Saathi

A chatbot that helps users understand Nepal's constitution using AI.

## Deployment Instructions

### Deploying to Streamlit Community Cloud

1. Create a GitHub account if you don't have one
2. Create a new repository on GitHub
3. Push your code to the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```
4. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
5. Sign in with your GitHub account
6. Click "New app"
7. Select your repository and branch
8. Set the main file path to `main.py`
9. Click "Deploy"

### Environment Variables

Make sure to set up your environment variables in Streamlit Cloud:
1. Go to your app's settings
2. Click on "Secrets"
3. Add your environment variables:
   ```
   HUGGINGFACE_API_KEY=your_api_key
   ```

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your environment variables:
   ```
   HUGGINGFACE_API_KEY=your_api_key
   ```

3. Run the app:
   ```bash
   streamlit run main.py
   ```

## Features

- PDF document processing
- Vector-based semantic search using Hugging Face models
- Conversational interface
- Source citation for answers
- Sample questions for quick access
- Responsive UI with dark/light mode support

## Project Structure

```
legal-ai-saathi/
├── docs/                    # PDF documents
│   └── nepal-constitution.pdf
├── utils/                   # Utility functions
│   ├── chat_utils.py       # Chat-related functions
│   └── document_loader.py  # PDF processing functions
├── .streamlit/             # Streamlit configuration
│   └── config.toml        # Theme and server settings
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
- torch
- huggingface-hub

## Development Workflow

1. Create a new branch for development:
   ```bash
   git checkout -b development
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Your commit message"
   ```

3. Push changes to the development branch:
   ```bash
   git push origin development
   ```

4. Create a pull request to merge into main branch

## License

MIT License 