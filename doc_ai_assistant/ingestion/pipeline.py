from app.ingestion.pdf_loader import extract_text
from app.ingestion.chunking import chunk_text

def ingest_document(file):
    # Step 1: PDF se text nikalo
    text = extract_text(file)

    # Step 2: Text ko chhote parts me todo
    chunks = chunk_text(text)

    return f"Document processed. Total chunks: {len(chunks)}"

