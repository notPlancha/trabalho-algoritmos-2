import networkx as nx

import Edge
from Graph import Graph, GraphG
from typing import List, Tuple
from UnionFind import UnionFind


# TODO do various ks, and compare with various methods
def kSpanningTree(graph: Graph, k: int) -> Graph:
    mst, edges = graph.kruskal(saveEdges=True)
    for e in edges[-(k - 1):]:
        mst.remove_edge(e)
    return mst


def louvain(graph: nx.Graph, k: int):
    pass  # TODO https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.louvain.louvain_communities.html#networkx.algorithms.community.louvain.louvain_communities


def fluid(graph: nx.Graph, k: int):
    pass  # TODO https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.asyn_fluid.asyn_fluidc.html#networkx.algorithms.community.asyn_fluid.asyn_fluidc


def draw_communities(graph: nx.Graph, communities: List[Tuple[int, int]], pos):  # TODO check if communities is of type
    pass  # TODO


if __name__ == "__main__":
    print(GraphG)
    print(kSpanningTree(GraphG, k=2))
