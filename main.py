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

    def __str__(self):
        return f"${str(self.__element)}$"
    def __repr__(self):
        return str(self)
class Edge:
    def __init__(self, Vertex1 : Vertex, Vertex2 : Vertex, peso : Real, isDirected = False):
        self.aresta : Tuple[Vertex, Vertex] = (Vertex1, Vertex2)
        self.peso = peso
        self.isDirected = isDirected
    def __getitem__(self, item):
        return self.aresta[item]

    def __str__(self):
        return f"%{str(self.aresta[0])} {('->' if self.isDirected else '<->')} {str(self.aresta[1])} ; peso = {self.peso}%"
    def __repr__(self):
        return str(self)
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
        if not isinstance(v, Vertex):
            v = Vertex(v)
        self._insert_vertex(v)
        return v
    def _insert_vertex(self, v: Vertex):
        self._vertices.add(v)
        self._map[v] = dict()
    def _insert_edge(self, e : Edge):
        if self.isDirected == e.isDirected:
            self._map[e.aresta[0]][e.aresta[1]] = e
            self._map[e.aresta[1]][e.aresta[0]] = e
            self._edges.add(e)
            return e
        else:
            raise AttributeError(f"Edge is{' not ' if not e.isDirected else ''}directed")
    def insert_edge(self, e : Edge, *args):
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


    def remove_edge(self, e : Edge):
        del self._map[e.aresta[0]][e.aresta[1]]
        del self._map[e.aresta[1]][e.aresta[0]]
        self._edges.remove(e)

    def remove_vertex(self, v : Vertex):
        del self._map[v]
        self._vertices.remove(v)
    def __str__(self):
        return str(self._map)
if __name__ == "__main__":
    g = Graph()
    v1 = g.insert_vertex(13)
    v2=g.insert_vertex(11)
    v3=g.insert_vertex(10)
    '''
    g.remove_vertex(v1)
    '''
    e1 = g.insert_edge(Edge(v1, v2, 10))
    e2 = g.insert_edge(Edge(v1, v3, 90))
    e3 = g.insert_edge(Edge(v2, v3, 67))
    '''
    g.remove_edge(e1)
    '''
    print(g.vertex_count())
    print(g.vertices())
    print(g.edges_count())
    print(g.edges())
    print(g.get_edge(v1, v2))
    print(g.degree(v1))
    '''
    print(g.outdegree(v1))
    print(g.indegree(v1))
    '''
    print(g)