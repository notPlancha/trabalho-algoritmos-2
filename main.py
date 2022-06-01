import warnings
from typing import Tuple, List
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


if __name__ == "__main__":
    # TODO: make usages
    """
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
    # random graph
    if "random" in args:
        import random

        if "--seed" in args:
            try:
                random.seed(int(args[args.index("--seed") + 1]))
            except ValueError:
                print("Seed must be an integer")
                sys.exit()
        G = Graph()
        for v in vertexList:
            G.insert_vertex(v)
        for _ in range(10):
            v1 = random.choice(vertexList)
            v2 = random.choice(vertexList)
            if v1 is not v2:
                GraphG.insert_edge(v1, v2, random.randint(1, 20))
        plt.figure()
        plt.title("Random graph")
        nx.draw(G.asNxGraph())
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

            # graoh
            fromFile = fromFile.disconnections()[0]
            clusters = kSpanningTree(fromFile, k)
            nxClusters: nx.Graph = clusters.asNxGraph()

            # seed
            if "--seed" in args:
                try:
                    seed = int(args[args.index("--seed") + 1])
                except ValueError:
                    sys.exit("Seed must be an integer")
            else:
                seed = None

            # iterations
            if "--iterations" in args:
                try:
                    iterations = int(args[args.index("--iterations") + 1])
                except ValueError:
                    sys.exit("iterations must be an integer")
            else:
                iterations = 30  # default

            # make pos # TODO used cache if ever gets fixed

            pos = nx.spring_layout(nxClusters, iterations=iterations, seed=seed)

            # draw
            plt.figure()
            plt.title("kSpanningTree(k={})".format(k))
            withLabels = "-no-labels" not in args
            nx.draw(nxClusters, with_labels=withLabels, pos=pos)
        # no mst
        else:
            # seed
            if "--seed" in args:
                try:
                    seed = int(args[args.index("--seed") + 1])
                except ValueError:
                    sys.exit("Seed must be an integer")
            else:
                seed = None

            # graph
            nxFromFile = fromFile.asNxGraph()
            nxFromFile: nx.Graph = clean(clusters(nxFromFile))[0]

            # pos
            if "-used-cached" in args:
                import json

                try:
                    with open("FacebookData/cachedPos.json", "r") as f:
                        pos = json.load(f)
                except FileNotFoundError:
                    sys.exit("Cached position file not found")
            else:
                if "--iterations" in args:
                    try:
                        iterations = int(args[args.index("--iterations") + 1])
                    except ValueError:
                        sys.exit("iterations must be an integer")
                else:
                    iterations = 30  # default
                pos = nx.spring_layout(nxFromFile, iterations=iterations, seed=seed, )
            # draw graph
            withLabels = "-no-labels" not in args
            plt.figure()
            plt.title("No clusters")
            nx.draw(nxFromFile, with_labels=withLabels, pos=pos, node_size=10, alpha=0.5)
    # commuities
    # TODO make iterations flag
    if "communities" in args:
        fromFile = Graph.from_csv("FacebookData/Data_Facebook.csv")
        if "--k" in args:
            try:
                k = int(args[args.index("--k") + 1])
            except ValueError:
                a = input("Enter k: ")
                if a.isdigit():
                    k = int(a)
                else:
                    sys.exit("k must be an integer")
        else:
            k = 5  # default
        # TODO

    if "-cache" in args:  # TODO remove if not possible
        try:
            try:
                import json

                with open("FacebookData/cachedPos.json", "w") as f:
                    f.write(json.dumps(pos))  # TODO doesn't work, dict has Vertexs as keys
            except NameError:
                print("No position to cache")
        except TypeError as e:
            warnings.warn("Error during cache:" + str(e))
    plt.show()
