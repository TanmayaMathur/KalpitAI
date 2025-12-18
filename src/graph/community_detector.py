# src/graph/community_detector.py

import networkx as nx
import community as community_louvain


def detect_communities(G):
    """
    Detect communities using Louvain algorithm
    """
    partition = community_louvain.best_partition(G)

    nx.set_node_attributes(G, partition, "community")

    return partition
