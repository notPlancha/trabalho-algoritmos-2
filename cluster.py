import networkx as nx
from networkx import minimum_spanning_tree
from networkx.algorithms.community import girvan_newman

import Edge
from Graph import Graph, GraphG
from typing import List, Tuple, Set
from UnionFind import UnionFind


# TODO do various ks, and compare with various methods
def kSpanningTree(graph: Graph, k: int) -> Graph:
    mst, edges = graph.kruskal(saveEdges=True)
    if k == 1:
        return mst
    for e in edges[-(k - 1):]:
        mst.remove_edge(e)
    return mst


def louvain(graph: nx.Graph, seed=None) -> List[Set]:
    return nx.algorithms.community.louvain_communities(graph, seed=seed)


def kcliques(nxFromFile, k):
    return nx.algorithms.community.k_clique_communities(nxFromFile, k)


if __name__ == "__main__":
    print(GraphG)
    print(kSpanningTree(GraphG, k=2))
