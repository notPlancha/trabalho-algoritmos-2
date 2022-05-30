from Graph import Graph, GraphG
from typing import List

class Cluster:
    def __init__(self, graph: Graph, clusterK : int, clusterN : int):
        #clusterK indicates the level of the cluster, clusterN indicates the number of the cluster in that level
        self.graph : Graph = graph
        self.name : str = f"Cluster {clusterK}-{clusterN}"
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self.graph)
    @staticmethod
    def DivisiveClustering(graph: Graph, MaxK: int) -> List["Cluster"]:
        #this will give kclusters for


def cluster(graph: Graph, maxClusters = 5):
    #Divisive clustering should be better since we have a 1000 person dataset and we're not interested in individuals



if __name__ == "__main__":
    print(cluster(GraphG))
