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
        for i in range(10):
            v1 = random.choice(vertexList)
            v2 = random.choice(vertexList)
            if v1 is not v2:
                GraphG.insert_edge(v1, v2, random.randint(1, 20))
    # main
    if "facebook" in args:
        fromFile = Graph.from_csv("FacebookData/Data_Facebook.csv")
        if "--k" in args:
            # k = 0 will return the MST with kruskal, else will return clusters
            try:
                k = int(args[args.index("--k") + 1])
            except ValueError:
                a = input("Enter k: ")
                if a.isdigit():
                    k = int(a)
                else:
                    sys.exit("k must be an integer")
            if k < 0: k = -k
            fromFile = fromFile.disconnections()[0]
            clusters = kSpanningTree(fromFile, k)
            nxClusters = clusters.asNxGraph()
            withLabels = "-no-labels" not in args
            if "--seed" in args:
                try:
                    seed = int(args[args.index("--seed") + 1])
                except ValueError:
                    sys.exit("Seed must be an integer")
            else:
                seed = None
            if "--iterations" in args:
                try:
                    iterations = int(args[args.index("--seed") + 1])
                except ValueError:
                    sys.exit("iterations must be an integer")
            else:
                iterations = 3000  # default
            pos = nx.spring_layout(nxClusters, iterations=iterations, seed=seed)
            nx.draw(nxClusters, with_labels=withLabels, pos=pos)
        else:
            if "--seed" in args:
                try:
                    seed = int(args[args.index("--seed") + 1])
                except ValueError:
                    sys.exit("Seed must be an integer")
            else:
                seed = None
            nxFromFile = fromFile.asNxGraph()
            nxFromFile: nx.Graph = clean(clusters(nxFromFile))[0]
            if "-used-cached" not in args:
                if "--iterations" in args:
                    try:
                        iterations = int(args[args.index("--seed") + 1])
                    except ValueError:
                        sys.exit("iterations must be an integer")
                else:
                    iterations = 3000  # default
                pos = nx.spring_layout(nxFromFile, iterations=3000, seed=seed)
            else:
                import json

                try:
                    with open("FacebookData/cachedPos.json", "r") as f:
                        pos = json.load(f)
                except FileNotFoundError:
                    sys.exit("Cached position file not found")
            withLabels = "-no-labels" not in args
            nx.draw(nxFromFile, with_labels=withLabels, pos=pos, node_size=10, alpha=0.5, )
    if "communities" in args:
        pass  # TODO
    try:
        if "-cache" in args:
            try:
                import json

                with open("FacebookData/cachedPos.json", "w") as f:
                    f.write(json.dumps(pos))  # TODO doesn't work, dict has Vertexs as keys
            except NameError:
                print("No position to cache")
    except TypeError as e:
        warnings.warn("Error during cache:" + str(e))
    plt.show()
