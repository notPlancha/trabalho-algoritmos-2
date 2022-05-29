from tkinter.tix import Tree
from typing import Tuple, Dict, Set, Iterable, Iterator
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
    def __init__(self, Vertex1: Vertex, Vertex2: Vertex, peso: Real, isDirected=False):
        self.aresta: Tuple[Vertex, Vertex] = (Vertex1, Vertex2)
        self.peso = peso
        self.isDirected = isDirected

    def __getitem__(self, item):
        return self.aresta[item]

    def __str__(self):
        return f"%{str(self.aresta[0])} {('->' if self.isDirected else '<->')} {str(self.aresta[1])} ; peso = {self.peso}%"

    def __repr__(self):
        return str(self)

    def endpoints(self):
        return self.aresta

    def opposite(self, v: Vertex):
        if self.aresta[0] is v:
            return self.aresta[1]
        elif self.aresta[1] is v:
            return self.aresta[0]
        else:
            raise AttributeError


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
                for i in self._map[v].values():
                    if i[0] is v:
                        yield i[1]
            else:
                for i in self._map[v].values():
                    if i[1] is v:
                        yield i[0]

    def insert_vertex(self, v: Vertex):
        if not isinstance(v, Vertex):
            v = Vertex(v)
        self._insert_vertex(v)
        return v

    def _insert_vertex(self, v: Vertex):
        # skips verification
        self._vertices.add(v)
        self._map[v] = dict()

    def _insert_edge(self, e: Edge):
        # skips verification
        if self.isDirected == e.isDirected:
            self._map[e.aresta[0]][e.aresta[1]] = e
            self._map[e.aresta[1]][e.aresta[0]] = e
            self._edges.add(e)
            return e
        else:
            raise AttributeError(f"Edge is{' not ' if not e.isDirected else ''}directed")

    def insert_edge(self, e: Edge, *args):
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
        return str(self._map)

    @staticmethod
    def fromEdges(edges: Iterable) -> "Graph":
        ret = Graph()
        for i in edges:
            ret._insert_vertex(i[0])
            ret._insert_vertex(i[1])
            ret._insert_edge(i)
        return ret

    def kruskal(self) -> "Graph":  # MST
        #TODO test
        # not checking if graph is disconnected
        if self.isDirected: raise AttributeError
        retVertices = set()
        retEdges = []
        orderedEdges = sorted(self._edges, key=lambda e: e.peso)
        for e in orderedEdges:
            if e[0] not in retVertices or e[1] not in retVertices:
                retVertices.update(e.aresta)
                retEdges.append(e)
        return Graph.fromEdges(retEdges)


if __name__ == "__main__":
    g = Graph()
    v1 = g.insert_vertex(13)
    v2 = g.insert_vertex(11)
    v3 = g.insert_vertex(10)
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
