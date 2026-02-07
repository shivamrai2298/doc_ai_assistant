from sentence_transformers import SentenceTransformer

# Model memory me ek hi baar load hoga
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    """
    chunks: list of strings
    returns: list of vectors (numbers)
    """
    embeddings = model.encode(chunks)
    return embeddings

