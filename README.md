
# Smart FAQ Chatbot with RAG & FastAPI

This is a smart and lightweight FAQ chatbot built using **FastAPI**, **Sentence-Transformers**, **FAISS**, and the **Aval AI GPT-4.1-mini API**.  
It leverages a hybrid RAG (Retrieval-Augmented Generation) pipeline that first checks for frequently asked questions and, if not matched, retrieves context from a custom dataset to generate accurate responses using an LLM.

---

## ✨ Features

- ✅ FastAPI backend
- ✅ FAQ matching with sentence similarity
- ✅ Contextual response generation via AvalAI GPT model
- ✅ RAG-style pipeline for hybrid answering
- ✅ Vector search using FAISS
- ✅ Supports multilingual input (via `paraphrase-multilingual-MiniLM-L12-v2`)

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```

You also need to download the SentenceTransformer model:

```bash
pip install sentence-transformers
```

---

## 🚀 Usage

Make sure you have the following files:

- `faq_clothing_store.json`: Contains question-answer pairs for FAQs.
- `dataset.json`: Contains long-form knowledge base sentences.

Then, run the FastAPI app:

```bash
uvicorn main:app --reload
```

Now, send POST requests to:

```
http://localhost:8000/chat
```

With this body:

```json
{
  "question": "Your user question here"
}
```

---

## 🧠 Example Workflow

1. User asks a question.
2. The system compares it to the FAQ dataset.
3. If a close match is found (based on vector similarity), it returns the predefined answer.
4. If not, it searches the long-form dataset for the most relevant content.
5. That context is passed to GPT for answer generation.

---

## 🔐 API Key

You need an [AvalAI API key](https://chat.avalai.ir/platform/api-keys) to use the GPT-4.1-mini model. Add your key in the code:

```python
API_KEY = "your-avalai-api-key"
```

---

## 📂 Folder Structure

```
.
├── main.py
├── faq_clothing_store.json
├── dataset.json
└── requirements.txt
```

---

## 📜 License

MIT — Feel free to use, share, and improve.

---

## 🤝 Contributions

PRs, issues, and stars are welcome :)
