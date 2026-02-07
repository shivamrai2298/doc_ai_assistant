from app.ingestion.pdf_loader import extract_text
from app.ingestion.chunking import chunk_text
from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import FAISSVectorStore

embedder = EmbeddingModel()
vector_store = FAISSVectorStore(embedding_dim=384)

def ingest_document(file):
    text = extract_text(file)
    chunks = chunk_text(text)

    embeddings = embedder.embed_texts(chunks)
    vector_store.add(embeddings, chunks)

    return {
        "status": "success",
        "chunks": len(chunks),
        "stored_vectors": len(embeddings)
    }
