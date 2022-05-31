import Edge
from Graph import Graph, GraphG
from typing import List, Tuple
from UnionFind import UnionFind




def kSpanningTree(graph: Graph, k: int = 5) -> Graph:
    mst, edges = graph.kruskal(saveEdges=True)
    for e in edges[-(k - 1):]:
        mst.remove_edge(e)
    return mst


if __name__ == "__main__":
    print(GraphG)
    print(kSpanningTree(GraphG, k=2))
