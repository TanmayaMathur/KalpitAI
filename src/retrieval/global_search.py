# src/retrieval/global_search.py

from collections import defaultdict


def global_search(graph, query_entities):
    """
    Retrieve relevant communities based on entity overlap
    """
    community_map = defaultdict(list)

    for node, data in graph.nodes(data=True):
        community = data.get("community")
        community_map[community].append(node)

    relevant_communities = []

    for community, nodes in community_map.items():
        score = sum(1 for ent in query_entities if ent in nodes)
        if score > 0:
            relevant_communities.append((community, score))

    relevant_communities.sort(key=lambda x: x[1], reverse=True)

    return [c[0] for c in relevant_communities[:3]]
