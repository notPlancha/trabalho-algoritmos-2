from typing import Tuple
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
    def __init__(self, Vertex1 : Vertex, Vertex2 : Vertex, peso : Real, isOneWay : bool = False):
        self.aresta : Tuple[Vertex, Vertex] = (Vertex1, Vertex2)
        self.isOneWay = isOneWay
        self.peso = peso
class Graph:
    def __init__(self, V = Vertex, E = Edge):
        self.V = V
        self.E = E