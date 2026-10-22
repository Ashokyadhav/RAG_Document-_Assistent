 📚 RAG Document Assistant

 📌 Project Overview

RAG Document Assistant is an AI-powered application that helps users understand PDF documents by asking questions in simple English.

Users can upload a PDF, ask questions about its content, and find relevant information from the document.

The application uses Retrieval-Augmented Generation (RAG) techniques to retrieve relevant text and help provide answers based on the uploaded document.

 ✨ Features

- Upload PDF documents of different types.
- Extract text from PDF files.
- Split large documents into smaller text chunks.
- Convert text into embeddings.
- Search for relevant information using FAISS.
- Ask questions about the uploaded document.
- Display relevant passages to help users verify the information.
- Help users find information without manually reading the entire document.

 🛠️ Technologies Used

- Python — Main programming language
- Streamlit — Web application interface
- PyPDF — Extract text from PDF documents
- Sentence Transformers** — Generate text embeddings
- FAISS — Search for relevant text efficiently
- Groq API — Planned integration for AI-generated answers

 ⚙️ How It Works

1. The user uploads a PDF document.
2. The application extracts text from the PDF.
3. The extracted text is divided into smaller chunks.
4. Sentence Transformers converts the chunks into embeddings.
5. FAISS searches for the most relevant chunks when the user asks a question.
6. The relevant passages are displayed to the user.
7. AI-generated answers based on the retrieved information will be integrated and tested.

 🎯 Use Cases

This application can help users explore different types of PDF documents, including:

- Educational materials and textbooks
- Research papers
- Business reports
- Company policies and manuals
- Technical documentation
- Study notes and reference materials

Note: The current version supports PDF uploads. Other document formats may be added in future versions.

🚀 Project Status

The project is currently under development. PDF uploading, text extraction, text chunking, embedding generation, and FAISS-based retrieval are being implemented in the Streamlit application.

AI-generated answers, testing, and online deployment are planned next steps.

👨‍💻 Author

Ashok Yadhav

GitHub: [Ashokyadhav](https://github.com/Ashokyadhav)
