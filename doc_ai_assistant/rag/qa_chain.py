from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import FAISSVectorStore
from transformers import pipeline

embedder = EmbeddingModel()

# ⚠️ Same vector store instance use hona chahiye
vector_store = FAISSVectorStore(embedding_dim=384)

llm = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_length=300
)

def answer_question(question: str):
    # Step 1: Question embedding
    query_embedding = embedder.embed_texts([question])[0]

    # Step 2: Retrieve relevant chunks
    relevant_chunks = vector_store.search(query_embedding, top_k=3)

    if not relevant_chunks:
        return "No relevant information found."

    # Step 3: Build context
    context = "\n".join(relevant_chunks)

    # Step 4: Ask LLM
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = llm(prompt)
    return response[0]["generated_text"]

