# TDS Virtual TA - PROJECT-1

A **Virtual Teaching Assistant** for the *Tools in Data Science (TDS)* course at **IIT Madras**, designed to automatically answer student questions using course materials and Discourse forum posts.


## 📌 Project Overview

This project implements a **Retrieval Augmented Generation (RAG)** system that assists Teaching Assistants by providing automatic, context-aware answers to student queries. It uses course content and student interactions from the Discourse forum to ensure accurate and relevant responses.


## 🚀 What We're Building

A FastAPI-based backend that:

- Accepts student questions (with optional file uploads)
- Retrieves relevant context from course content and Discourse discussions
- Generates a helpful response using a language model


## 🔧 Key Components

- **Data Collection**  
  Extracts relevant data from Discourse posts and TDS course content (slides, markdown files).

- **Text Preprocessing**  
  Cleans and structures the text, generating embeddings for efficient similarity search.

- **RAG System**  
  Combines retrieval and generation to produce high-quality answers.

- **FastAPI Application**  
  Exposes endpoints for question input, runs the retrieval + generation pipeline.

- **Deployment with Vercel**  
  Deployed and accessible via public URL.



## 📚 Data Sources

- **Course Content:**  
  Tools in Data Science (TDS) – *Jan 2025 term*, as available on **15 April 2025**.

- **Discourse Posts:**  
  Collected from **1 Jan 2025** to **14 Apr 2025**.

---


## ⚙️ Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shivam-Brahmkshatriya/TDS-PROJECT-1.git
cd TDS-PROJECT-1
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables (.env)
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Preprocess the Data
```bash
python preprocess.py
```

### 5. Run the FastAPI App
```bash
uvicorn app:app --reload
```

---

## 🌐 Live Deployment
## 👉 https://tds-project-1-delta.vercel.app

---

## 🙌 Acknowledgements
This project was built as part of the Tools in Data Science (TDS) course for the IIT Madras BS in Data Science & Applications program.

## 📝 License
This project is intended for academic use only, respecting the content and intellectual property rights of IIT Madras.

---
