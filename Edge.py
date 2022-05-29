from Vertex import Vertex
from typing import Tuple
from numbers import Real


class Edge:
    def __init__(self, Vertex1: Vertex, Vertex2: Vertex, peso: Real, isDirected=False):
        self.aresta: Tuple[Vertex, Vertex] = (Vertex1, Vertex2)
        self.peso = peso
        self.isDirected = isDirected

    def __getitem__(self, item):
        return self.aresta[item]

    def __str__(self):
        return f"{str(self.aresta[0])} {('->' if self.isDirected else '<->')} {str(self.aresta[1])}; peso = {self.peso}"

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
