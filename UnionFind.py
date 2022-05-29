from typing import Dict, Set
from Vertex import Vertex

class UnionFind:
    def __init__(self, vertices: Set[Vertex]):
        self.__parent: Dict[Vertex, Vertex] = dict()
        self.__rank: Dict[Vertex, int] = dict()
        self.__size: Dict[Vertex, int] = dict()
        for v in vertices:
            self.__make_set(v)

    def __make_set(self, v: Vertex) -> None:
        self.__parent[v] = v
        self.__rank[v] = 0
        self.__size[v] = 1

    def find(self, v: Vertex) -> Vertex:
        if self.__parent[v] is not v:
            self.__parent[v] = self.find(self.__parent[v])
        return self.__parent[v]

    def union(self, v1: Vertex, v2: Vertex) -> None:
        v1_root = self.find(v1)
        v2_root = self.find(v2)
        if v1_root is v2_root:
            return
        if self.__rank[v1_root] > self.__rank[v2_root]:
            self.__parent[v2_root] = v1_root
            self.__size[v1_root] += self.__size[v2_root]
        else:
            self.__parent[v1_root] = v2_root
            self.__size[v2_root] += self.__size[v1_root]
            if self.__rank[v1_root] == self.__rank[v2_root]:
                self.__rank[v2_root] += 1

    def __str__(self):
        return f"{self.__parent}"