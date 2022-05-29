from Graph import Graph, GraphG
from typing import List


def cluster(graph: Graph, ):
    #bad way to do it, change it later
    table: List[List[int]] = [[0] * graph.vertex_count() for _ in range(graph.vertex_count())]
    headers = list(graph.vertices())
    for e in graph.edges():
        indexE0 = headers.index(e.aresta[0])
        indexE1 = headers.index(e.aresta[1])
        table[indexE0][indexE1] = e.peso  # aqui o peso equivale à distancia
        table[i[1]][i[0]] = 1

    print(table)


if __name__ == "__main__":
    print(cluster(GraphG))
