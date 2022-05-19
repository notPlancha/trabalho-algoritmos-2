from typing import Tuple, Dict, Set, Iterable
from numbers import Real

class Vertex:
    def __init__(self, e):
        self.__element = e

    @property
    def id(self):
        return hash(self)

    @property
    def element(self):
        return self.__element

    def __hash__(self):
        return hash(id(self))

class Edge:
    def __init__(self, Vertex1 : Vertex, Vertex2 : Vertex, peso : Real, isDirected = False):
        self.aresta : Tuple[Vertex, Vertex] = (Vertex1, Vertex2)
        self.peso = peso
        self.isDirected = isDirected
    def __getitem__(self, item):
        return self.aresta[item]
class Graph:
    def __init__(self, isDirected = False):
        self._map : Dict[Vertex, Dict[Vertex, Edge]] = dict()
        self._edges : Set[Edge] = set()
        self._vertices : Set[Vertex] = set()
        self.isDirected : bool = isDirected
    def vertex_count(self):
        return len(self._vertices)
    def vertices(self) -> Iterable:
        return self._vertices
    def edges_count(self):
        return len(self._edges)
    def edges(self) -> Iterable:
        return self._edges
    def get_edge(self, u : Vertex, v : Vertex) -> Edge:
        return self._map[u][v]
    def degree(self, v: Vertex):
        return len(self._map[v])
    def indegree(self, v: Vertex) -> int:
        if not self.isDirected: raise AttributeError("Graph is not directed")
        return sum(b for a, b in self._map[v] if b[1] is v)
    def outdegree(self, v: Vertex) -> int:
        if not self.isDirected: raise AttributeError("Graph is not directed")
        return sum(b for a, b in self._map[v] if b[0] is v)
    def insert_vertex(self, v : Vertex):
        self._vertices.add(v)
        self._map[v] = dict()

    def insert_edge(self, e : Edge):
        if self.isDirected == e.isDirected:
            self._map[e.aresta[0]][e.aresta[1]] = e
            self._map[e.aresta[1]][e.aresta[0]] = e
            self._edges.add(e)
        else:
            raise AttributeError(f"Edge is{' not ' if not e.isDirected else ''}directed")

    def remove_edge(self, e : Edge):
        del self._map[e.aresta[0]][e.aresta[1]]
        del self._map[e.aresta[1]][e.aresta[0]]
        self._edges.remove(e)

    def remove_vertex(self, v : Vertex):
        del self._map[v]
        self._vertices.remove(v)