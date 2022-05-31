from typing import Tuple, List
from Graph import GraphG, Graph, l as vertexList
import networkx as nx
import matplotlib.pyplot as plt
from cluster import kSpanningTree
import sys

if __name__ == "__main__":
    # TODO: make usages
    """
    usage: 
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
    # File
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
    if "facebook" in args:
        fromFile = Graph.from_csv("FacebookData/Data_Facebook.csv")
        if "--k" in args:
            # k = 0 will return the MST with kruskal
            try:
                k = int(args[args.index("--k") + 1])
            except ValueError:
                a = input("Enter k: ")
                if a.isdigit(): k = int(a)
                else:
                    sys.exit("k must be an integer")
            if k < 0: k = -k
            clusters = kSpanningTree(fromFile, k)
            print(clusters)
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
                iterations = 3000 #default
            pos = nx.spring_layout(nxClusters, dim=100, iterations=iterations, seed=seed)
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
            if "-used-cached" not in args:
                pos = nx.spring_layout(nxFromFile, dim=2, iterations=3000, seed=seed)
            else:
                import json
                try:
                    with open("FacebookData/cachedPos.json", "r") as f:
                        pos = json.load(f)
                except FileNotFoundError:
                    sys.exit("Cached position file not found")
            withLabels = "-no-labels" not in args
            nx.draw(nxFromFile, with_labels=withLabels, pos=pos)
        if "-cache" in args:
            import json
            with open("FacebookData/cachedPos.json", "w") as f:
                f.write(json.dumps(pos))
    plt.show()
