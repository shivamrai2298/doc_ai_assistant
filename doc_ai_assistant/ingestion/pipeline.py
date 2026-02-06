from app.ingestion.pdf_loader import extract_text
from app.ingestion.chunking import chunk_text

def ingest_document(file):
    text = extract_text(file)
    chunks = chunk_text(text)

    return f"Document processed. Total chunks: {len(chunks)}"

