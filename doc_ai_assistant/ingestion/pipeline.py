from app.ingestion.pdf_loader import extract_text
from app.ingestion.chunking import chunk_text
from rag.embeddings import generate_embeddings

def ingest_document(file):
    # Step 1: Text extract
    text = extract_text(file)

    # Step 2: Chunking
    chunks = chunk_text(text)

    # Step 3: Embeddings
    embeddings = generate_embeddings(chunks)

    return f"""
    Document processed.
    Chunks: {len(chunks)}
    Embeddings created: {len(embeddings)}
    """
