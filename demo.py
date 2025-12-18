# demo.py

import json

from src.graph.graph_builder import build_knowledge_graph
from src.graph.community_detector import detect_communities
from src.graph.entity_extractor import extract_entities

from src.retrieval.local_search import local_search
from src.retrieval.global_search import global_search
from src.llm.answer_generator import generate_answer

# Load chunks
with open("data/processed/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

print("📚 Chunks loaded:", len(chunks))

# Build graph
G = build_knowledge_graph(chunks)
detect_communities(G)

while True:
    question = input("\n❓ Ask a question (or type 'exit'): ")
    if question.lower() == "exit":
        break

    # Entity extraction from query
    query_entities = extract_entities(question)

    # Global search (communities)
    communities = global_search(G, query_entities)

    # Local search (chunks)
    while True:
        question = input("\n❓ Ask a question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        relevant_chunks, confidence = local_search(chunks, question, top_k=5)

        if not relevant_chunks:
            print("\n🧠 Answer:")
            print(
                "I cannot answer this question because it is not covered "
                "in Dr. B. R. Ambedkar’s writings."
            )
            continue   # ✅ NOW THIS IS VALID

        answer = generate_answer(relevant_chunks, question)
        print("\n🧠 Answer:")
        print(answer)
