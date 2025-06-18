# TDS Virtual TA - PROJECT-1

A **Virtual Teaching Assistant** for the *Tools in Data Science (TDS)* course at **IIT Madras**, designed to automatically answer student questions using course materials and Discourse forum posts.

---

## 📌 Project Overview

This project implements a **Retrieval Augmented Generation (RAG)** system that assists Teaching Assistants by providing automatic, context-aware answers to student queries. It uses course content and student interactions from the Discourse forum to ensure accurate and relevant responses.

---

## 🚀 What We're Building

A FastAPI-based backend that:

- Accepts student questions (with optional file uploads)
- Retrieves relevant context from course content and Discourse discussions
- Generates a helpful response using a language model

---

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

---

## 📚 Data Sources

- **Course Content:**  
  Tools in Data Science (TDS) – *Jan 2025 term*, as available on **15 April 2025**.

- **Discourse Posts:**  
  Collected from **1 Jan 2025** to **14 Apr 2025**.

---

## 📁 Project Structure
├── downloaded_threads/ # Downloaded Discourse threads (JSON)
├── markdown_files/ # Processed course content files (Markdown)
├── .env # Environment variables (e.g., API keys)
├── preprocess.py # Script for preprocessing and DB generation
├── app.py # FastAPI server application
├── requirements.txt # Project dependencies
├── .gitignore # Files to ignore in Git
└── vercel.json # Deployment configuration for Vercel

