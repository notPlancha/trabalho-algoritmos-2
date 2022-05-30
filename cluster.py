import Edge
from Graph import Graph, GraphG
from typing import List, Tuple
from UnionFind import UnionFind


def GirvanNewman(graph : Graph, maxK : int = 5) -> List[Tuple[int, Graph]]: # each graph is a level of each k
    # divisive hierarchical method
    #TODO
    pass
def kSpanningTree(graph : Graph, k: int = 5) -> Graph:
    mst, edges = graph.kruskal(saveEdges=True)
    for e in edges[-(k-1):]:
        mst.remove_edge(e)
    return mst

def singleLinkage(graph : Graph, minK: int = 5) -> List[Tuple[int, Graph]]:
    # aglomerative hiearchical method
    #TODO
    pass


if __name__ == "__main__":
    print("Hello from cluster.py")
