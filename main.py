import random
import warnings
from typing import Tuple, List

import numpy

import cluster
from Graph import GraphG, Graph, l as vertexList
import networkx as nx
import matplotlib.pyplot as plt
from cluster import kSpanningTree
import sys


def clean(G: List[nx.Graph]):
    # Removes little clusters that are not connected with main
    for i in G:
        if i.number_of_edges() <= 3:
            G.remove(i)
    return G


def clusters(G: nx.Graph) -> List[nx.Graph]:
    return list((G.subgraph(c) for c in nx.connected_components(G)))

def getIterations(args):
    if "--iterations" in args:
        try:
            iterations = int(args[args.index("--iterations") + 1])
        except ValueError:
            sys.exit("iterations must be an integer")
    else:
        iterations = 30  # default
    return iterations
def getSeed(args):
    if "--seed" in args:
        try:
            seed = int(args[args.index("--seed") + 1])
        except ValueError:
            sys.exit("seed must be an integer")
    else:
        seed = None  # default
    return seed
def getLabels(args):
    return "-no-labels" not in args

if __name__ == "__main__":
    # TODO: make usages
    usages = """
    usage: 
    example: show an example graph
    ramdom: create a random graph
    --debug: step by step
    --seed: make a seed
    facebook: graph with data given
    --k: make sub graphs
    -no-labels: 
    --iterations: iterate a graph
    
    """
    args = sys.argv[1:]
    if len(args) == 0:
        print(usages)
        sys.exit()
    if "--debug" in args:
        DEBUG = True

    # GraphG small example
    if "example" in args:
        print("GraphG")
        print(GraphG)
        nxGraghG = GraphG.asNxGraph()
        print(nxGraghG)
        plt.figure()
        plt.title("GraphG")
        nx.draw(nxGraghG)
    # main
    if "facebook" in args:
        fromFile = Graph.from_csv("FacebookData/Data_Facebook.csv")
        # k = 1 will return the MST with kruskal, else will return clusters from kSpanningTree
        if "--k" in args:
            # get k
            try:
                k = int(args[args.index("--k") + 1])
            except ValueError:
                a = input("Enter k: ")
                if a.isdigit():
                    k = int(a)
                else:
                    sys.exit("k must be an integer")
            if k < 0: k = -k

            # graph
            clusterss = kSpanningTree(fromFile, k)
            nxClusters: nx.Graph = clusterss.asNxGraph()
            nxClusters = clean(clusters(nxClusters))[0]

            # make pos
            pos = nx.spring_layout(nxClusters, iterations=getIterations(args), seed=getSeed(args))

            # draw
            plt.figure()
            plt.title("kSpanningTree(k={})".format(k))
            nx.draw(nxClusters, with_labels=getLabels(args), pos=pos, node_size=10, alpha=0.5)
        # no mst
        else:

            # graph
            nxFromFile = fromFile.asNxGraph()
            nxFromFile: nx.Graph = clean(clusters(nxFromFile))[0]

            # pos

            pos = nx.spring_layout(nxFromFile, iterations=getIterations(args), seed=getSeed(args), )
            # draw graph
            plt.figure()
            plt.title("No clusters")
            nx.draw(nxFromFile, with_labels=getLabels(args), pos=pos, node_size=10, alpha=0.5)
    # commuities
    if "communities" in args:
        fromFile = Graph.from_csv("FacebookData/Data_Facebook.csv")
        try:
            typee = args[args.index("communities") + 1]
        except IndexError:
            sys.exit("No type specified")
        nxFromFile = fromFile.asNxGraph()
        nxFromFile: nx.Graph = clean(clusters(nxFromFile))[0]
        if typee == "louvain":
            commuities = cluster.louvain(nxFromFile, getSeed(args))
        elif typee == "modularity":
            commuities = cluster.modularity(nxFromFile)
        else:
            sys.exit("Type must be louvain or modularity")
        pass #TODO test
        pos = nx.spring_layout(nxFromFile, iterations=getIterations(args), seed=getSeed(args))
        labels = getLabels(args)
        for i in commuities:
            nx.draw_networkx_nodes(nxFromFile,
                                   pos,
                                   nodelist=i,
                                   node_color=[[random.random(), random.random(), random.random()]],
                                   node_size=10,
                                   alpha=0.2)
        nx.draw_networkx_edges(nxFromFile, pos, alpha=0.5)
        if labels: nx.draw_networkx_labels(nxFromFile, pos)
    # in-comunities #TODO fazer se tiver tempo
    if "in-comunities" in args:
        warnings.warn("inCouminties not implemented", DeprecationWarning)
        pass
    plt.show()
