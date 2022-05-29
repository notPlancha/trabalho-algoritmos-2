from Edge import Edge
from Vertex import Vertex
from typing import Dict, Set, Iterable
from UnionFind import UnionFind

DEBUG: bool = False


class Graph:
    # Simple gragh
    def __init__(self, isDirected=False):
        self._map: Dict[Vertex, Dict[Vertex, Edge]] = dict()
        self._edges: Set[Edge] = set()
        self._vertices: Set[Vertex] = set()
        self.isDirected: bool = isDirected

    def vertex_count(self):
        return len(self._vertices)

    def vertices(self) -> Iterable:
        return self._map.keys()  # faster than iterating from the set (prob)

    def edges_count(self):
        return len(self._edges)

    def edges(self) -> Iterable:
        return self._edges

    def get_edge(self, u: Vertex, v: Vertex) -> Edge:
        uD = self._map.get(u)
        if uD is not None:
            return uD.get(v)

    def degree(self, v: Vertex, out=None):
        if out is None:
            return len(self._map[v])
        else:
            if not self.isDirected:
                raise AttributeError("Graph is not directed")
            elif out:
                return sum(b for a, b in self._map[v] if b[0] is v)
            else:
                return sum(b for a, b in self._map[v] if b[1] is v)

    def incident_edges(self, v: Vertex, out: bool | None = None) -> Iterable:
        if out is None:
            return self._map[v].values()
        else:
            if not self.isDirected:
                raise AttributeError("Graph is not directed")
            elif out:
                for e in self._map[v].values():
                    if e[0] is v:
                        yield e[1]
            else:
                for e in self._map[v].values():
                    if e[1] is v:
                        yield e[0]

    def insert_vertex(self, v: Vertex) -> Vertex:
        if not isinstance(v, Vertex):
            v = Vertex(v)
        self._insert_vertex(v)
        return v

    # returns False if vertex was already in the graph
    def _insert_vertex(self, v: Vertex) -> bool:
        # skips argument verification
        if v in self._vertices: return False
        self._vertices.add(v)
        self._map[v] = dict()
        return True

    # returns False if edge was already in the graph
    def _insert_edge(self, e: Edge) -> bool:
        # skips argument verification
        if e in self._edges: return False
        if self.isDirected != e.isDirected: raise AttributeError(
            f"Edge is{' not ' if not e.isDirected else ''}directed")
        self._map[e.aresta[0]][e.aresta[1]] = e
        self._map[e.aresta[1]][e.aresta[0]] = e
        self._edges.add(e)
        return True

    def insert_edge(self, e: Edge, *args) -> Edge:
        if not isinstance(e, Edge):
            if not isinstance(e, tuple):
                try:
                    e = Edge(e, args[0], args[1])
                except:
                    raise TypeError
            else:
                try:
                    e = Edge(*e)
                except:
                    raise TypeError
        self._insert_edge(e)
        return e

    def remove_edge(self, e: Edge):
        del self._map[e.aresta[0]][e.aresta[1]]
        del self._map[e.aresta[1]][e.aresta[0]]
        self._edges.remove(e)

    def remove_vertex(self, v: Vertex):
        vEdges = self._map[v]
        self._vertices.remove(v)
        self._edges.difference_update(vEdges.values())
        for i in vEdges.keys():
            del self._map[i][v]
        del self._map[v]

    def __str__(self):
        ret = "Graph:\n"
        for i in self._vertices:
            ret += f"{i}\n"
            for i in self._map[i].values():
                ret += f"\t{i}\n"
            ret += "\n"
        ret += f"Vertices: {len(self._vertices)}\n"
        ret += f"Edges: {len(self._edges)}\n"
        return ret

    def kruskal(self) -> "Graph":  # MST
        if self.isDirected: raise AttributeError
        forest = UnionFind(self._vertices)
        if DEBUG: print(forest)
        ret = Graph()
        orderedEdges = sorted(self._edges, key=lambda e: e.peso)
        for e in orderedEdges:
            if not forest.find(e.aresta[0]) is forest.find(e.aresta[1]):
                if DEBUG: print(e)
                ret._insert_vertex(e.aresta[0])
                ret._insert_vertex(e.aresta[1])
                ret._insert_edge(e)
                forest.union(e.aresta[0], e.aresta[1])
                if DEBUG: print(forest)
        return ret


if __name__ == "__main__":
    g = Graph()
    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    E = Vertex("E")
    F = Vertex("F")
    G = Vertex("G")
    for i in [A, B, C, D, E, F, G]:
        g.insert_vertex(i)
    g.insert_edge(Edge(C, E, 1))
    g.insert_edge(Edge(A, B, 2))
    g.insert_edge(Edge(A, C, 3))
    g.insert_edge(Edge(A, D, 3))
    g.insert_edge(Edge(B, E, 3))
    g.insert_edge(Edge(B, C, 4))
    g.insert_edge(Edge(C, D, 5))
    g.insert_edge(Edge(D, F, 7))
    g.insert_edge(Edge(F, E, 8))
    g.insert_edge(Edge(F, G, 9))
    print(g)
    print(g.kruskal())
