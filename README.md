# README.md

## 🧠 AI PDF Summarizer – Monorepo

A full-stack PDF summarization tool that uses NLP to summarize content and generate quiz questions from uploaded PDFs. Built using microservices with FastAPI, Celery, MongoDB, PostgreSQL, and React.

---

### 🧾 Features
- Upload PDFs and extract text
- Summarize content using Transformer models (e.g., BART, T5)
- Auto-generate questions (quiz) based on summarized content *(coming soon)*
- Async background processing using Celery and Redis
- JWT-based authentication (in progress)

---

### ⚙️ Technologies Used
- **FastAPI** for backend microservices
- **Transformers (Hugging Face)** for summarization and NLP
- **Celery + Redis** for async processing
- **MongoDB** for summaries & documents
- **PostgreSQL** for user data (in auth service)
- **React + Tailwind CSS** for frontend

---
