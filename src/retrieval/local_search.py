# src/retrieval/local_search.py

from .vector_store import VectorStore
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_NAME = "all-MiniLM-L6-v2"


def local_search(chunks, query, top_k=5, min_similarity=0.4):
    store = VectorStore(chunks)
    results = store.search(query, top_k=top_k)

    model = SentenceTransformer(MODEL_NAME)
    query_vec = model.encode([query])
    chunk_vecs = model.encode(results)

    similarities = cosine_similarity(query_vec, chunk_vecs)[0]

    max_sim = max(similarities)

    # 🔴 Relevance gate
    if max_sim < min_similarity:
        return [], max_sim

    return results, max_sim
