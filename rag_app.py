
import streamlit as st

st.set_page_config(
    page_title="RAG Document Assistant",
    page_icon="📚"
)

st.title("📚 RAG Document Assistant")

st.write(
    "Upload a college document and ask questions about it."
)

st.subheader("1. Upload your college PDF")

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

