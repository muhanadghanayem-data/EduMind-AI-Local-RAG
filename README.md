# 🎓 EduMind AI: Your Ultimate Interactive Textbook Companion

EduMind AI is a fully local, private, and zero-cost RAG (Retrieval-Augmented Generation) system built to transform textbook reading into an interactive AI chat experience. 

## ✨ Key Features
- **100% Local & Private:** Runs entirely on the user's hardware (via Ollama). No data leaves your machine.
- **Zero API Costs:** Built using open-source models, completely eliminating OpenAI/Anthropic subscription fees.
- **Math-Aware Prompting:** Specially optimized to handle distorted mathematical notations (like integration symbols) from PDF extractors and retrieve correct numeric answers.
- **Old Money Design:** Features a customized, minimalist dark user interface tailored with Scandinavian-inspired typography.

## 🛠️ Tech Stack
- **Framework:** LangChain
- **LLM Engine:** Meta's Llama 3 (via Ollama)
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
- **Vector Store:** ChromaDB
- **User Interface:** Streamlit

## 🚀 How to Run Locally

1. **Clone the repository and install dependencies:**
```bash
pip install streamlit ollama langchain-community langchain-ollama pypdf chromadb sentence-transformers
```

2. **Ensure Ollama is running Llama 3 in the background:**
```bash
ollama run llama3
```

3. **Launch the application:**
```bash
streamlit run app.py
```
