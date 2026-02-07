import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FAISSVectorStore:
    def __init__(self, dim: int = 384):
        """
        dim = embedding size
        all-MiniLM-L6-v2 → 384
        """
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

    def add_texts(self, texts: list[str]):
        embeddings = self.model.encode(texts)
        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)
        self.text_chunks.extend(texts)

    def similarity_search(self, query: str, k: int = 5):
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.text_chunks):
                results.append(self.text_chunks[idx])

        return results

