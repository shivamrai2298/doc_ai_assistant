from app.ingestion.pdf_loader import extract_text
from app.ingestion.chunking import chunk_text
from app.rag.embeddings import EmbeddingModel

embedder = EmbeddingModel()

def ingest_document(file):
    text = extract_text(file)
    chunks = chunk_text(text)

    embeddings = embedder.embed_texts(chunks)

    return {
        "chunks": len(chunks),
        "embedding_vectors": len(embeddings)
    }
