# src/pipeline/ambedkargpt.py

import json
import os

from src.chunking.semantic_chunker import semantic_chunking
from src.graph.graph_builder import build_knowledge_graph
from src.graph.community_detector import detect_communities

PDF_PATH = "data/Ambedkar_book.pdf"
OUTPUT_DIR = "data/processed"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Phase 1: Semantic Chunking
    sentences, chunks = semantic_chunking(
        pdf_path=PDF_PATH,
        buffer_size=3,
        similarity_threshold=0.75,
        max_sentences_per_chunk=8
    )

    with open(f"{OUTPUT_DIR}/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"✅ Semantic Chunking Complete: {len(chunks)} chunks")

    # Phase 2: Knowledge Graph
    G = build_knowledge_graph(chunks)
    communities = detect_communities(G)

    print(f"✅ Knowledge Graph Built")
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    print(f"Communities: {len(set(communities.values()))}")


if __name__ == "__main__":
    main()
