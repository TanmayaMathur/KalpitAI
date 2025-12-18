# src/retrieval/vector_store.py

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"


class VectorStore:
    def __init__(self, chunks):
        self.model = SentenceTransformer(MODEL_NAME)
        self.chunks = chunks
        self.embeddings = self.model.encode(chunks)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def search(self, query, top_k=5):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(query_vec, top_k)
        return [self.chunks[i] for i in indices[0]]
