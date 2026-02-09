import faiss
import pickle
import os

class FaissVectorStore:
    def __init__(self, dim, index_path="data/index.faiss", text_path="data/texts.pkl"):
        self.dim = dim
        self.index_path = index_path
        self.text_path = text_path

        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            with open(text_path, "rb") as f:
                self.texts = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(dim)
            self.texts = []

    def add(self, embeddings, chunks):
        self.index.add(embeddings)
        self.texts.extend(chunks)

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.text_path, "wb") as f:
            pickle.dump(self.texts, f)

    def search(self, query_embedding, k=5):
        D, I = self.index.search(query_embedding, k)
        return [self.texts[i] for i in I[0]]
