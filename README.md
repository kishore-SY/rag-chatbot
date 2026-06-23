# 🧠 RAG Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG) Chatbot** built using **Python, Streamlit, LangChain, FAISS, and Gemini API**.
This chatbot allows users to securely log in, process documents, and ask intelligent questions based on document content using semantic search and Large Language Models (LLMs).

---

## 🚀 Live Demo

Deployed App: https://rag-chatbot-4mu9ekgmyfvmwfgek6kjpg.streamlit.app/

---

## 📌 Features

✅ User Authentication (Login / Register)
✅ Secure password hashing using bcrypt
✅ PDF document ingestion
✅ Vector database using FAISS
✅ Semantic search with embeddings
✅ Context-aware AI responses using Gemini API
✅ Interactive Streamlit UI
✅ Retrieval-Augmented Generation pipeline

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / ML

* LangChain
* Google Gemini API
* Sentence Transformers
* FAISS

### Authentication

* bcrypt
* JSON-based user storage

---

## 📂 Project Structure

```bash
rag-chatbot/
│
├── app.py                # Main Streamlit app
├── auth.py               # Login/Register authentication
├── config.py             # Configuration & API keys
├── ingest.py             # PDF processing and chunking
├── rag_pipeline.py       # RAG pipeline logic
├── users.json            # User data storage
├── requirements.txt      # Dependencies
│
├── data/                 # Source documents
├── vectorstore/          # FAISS vector database
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/kishore-SY/rag-chatbot.git
cd rag-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Get API key from Google AI Studio.

### 5. Run Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User uploads or loads PDF documents
2. Documents are split into chunks
3. Chunks are converted into embeddings
4. Embeddings stored in FAISS vector database
5. User asks question
6. Relevant chunks retrieved using similarity search
7. Gemini LLM generates accurate answer from retrieved context

---


### Login Page
![Login Page](screenshots/login-page.png)

### Chat Interface
![Chat Interface](screenshots/chat-page.png)


---

## 🔮 Future Improvements

* Multi-document upload
* Chat history
* Admin dashboard
* Database integration (MongoDB / PostgreSQL)
* Better UI/UX
* Docker deployment

---

## 👨‍💻 Author

**Kishore A**
Aspiring AI Engineer | Python Developer | GenAI Enthusiast

GitHub: https://github.com/kishore-SY

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
