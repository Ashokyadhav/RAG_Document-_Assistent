
import streamlit as st

st.set_page_config(
    page_title="RAG Document Assistant",
    page_icon="📚"
)

st.title("📚 RAG Document Assistant")

st.write(
    "Upload any PDF document and ask questions about its content."
)

st.subheader("1. Upload your PDF document")

uploaded_file = st.file_uploader(
    "Choose a PDF document",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

    from pypdf import PdfReader

    pdf_reader = PdfReader(uploaded_file)

    document_text = ""

    for page in pdf_reader.pages:
        document_text += page.extract_text() or ""

    st.write("Total characters extracted:", len(document_text))

    # Split the PDF text into smaller chunks
    chunk_size = 1000
    overlap = 200

    chunks = []

    for start in range(0, len(document_text), chunk_size - overlap):
        chunk = document_text[start:start + chunk_size]

        if chunk.strip():
            chunks.append(chunk)

    st.write("Total text chunks created:", len(chunks))

    # Convert text chunks into embeddings
    from sentence_transformers import SentenceTransformer

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    chunk_embeddings = embedding_model.encode(chunks)

    st.success("Text embeddings created successfully!")

    # Create a FAISS search index
    import faiss
    import numpy as np

    chunk_embeddings = np.array(
        chunk_embeddings
    ).astype("float32")

    faiss_index = faiss.IndexFlatL2(
        chunk_embeddings.shape[1]
    )

    faiss_index.add(chunk_embeddings)

    st.success("FAISS search index created successfully!")
    st.subheader("2. Ask a question")

    question = st.text_input(
        "Enter your question about the PDF"
    )

    if question:
        question_embedding = embedding_model.encode(
            [question]
        ).astype("float32")

        distances, indices = faiss_index.search(
            question_embedding, 3
        )

        relevant_chunks = [
            chunks[i] for i in indices[0]
            if i < len(chunks)
        ]

        st.subheader("Relevant PDF information")

        for chunk in relevant_chunks:
            st.write(chunk)

    st.subheader("3. AI Answer")
    if not question:
        st.info("Enter a question above to get an AI answer.")
        st.stop()

    from groq import Groq

    import os

    api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))

    if not api_key:
        st.error("Groq API key is not configured.")
    else:
        client = Groq(api_key=api_key)

        context = "\n\n".join(relevant_chunks)

        prompt = f"""
        Answer the question using only the context below.
        If the answer is not in the context, say:
        "I could not find this information in the uploaded PDF."

        Context:
        {context}

        Question:
        {question}
        """

        with st.spinner("Generating answer..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.write(response.choices[0].message.content)
