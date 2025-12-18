# src/graph/graph_builder.py

import networkx as nx
from .entity_extractor import extract_entities, extract_relations


def build_knowledge_graph(chunks):
    """
    Build a knowledge graph from semantic chunks
    """
    G = nx.Graph()

    for chunk in chunks:
        entities = extract_entities(chunk)
        relations = extract_relations(chunk)

        # Add entities as nodes
        for entity in entities:
            if not G.has_node(entity):
                G.add_node(entity, type="entity")

        # Add relations as edges
        for subj, verb, obj in relations:
            G.add_edge(subj, obj, relation=verb)

    return G
