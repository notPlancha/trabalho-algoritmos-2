from typing import Tuple, List
from Graph import GraphG, Graph
from networkx import draw_networkx as draw, draw_networkx_labels as draw_labels
import networkx as nx
import matplotlib.pyplot as plt
from cluster import kSpanningTree


if __name__ == "__main__":
    print(GraphG)
    nxGraphG = GraphG.asNxGraph()
    pos = nx.spring_layout(nxGraphG)
    draw(nxGraphG, pos, with_labels=True, node_color=(1,1,1,1))
    labels = nx.get_edge_attributes(nxGraphG, 'weight')
    nx.draw_networkx_edge_labels(nxGraphG, pos, edge_labels=labels)
    plt.figure(2)
    draw(GraphG.kruskal()[0].asNxGraph(), with_labels=True, node_color=(1,1,1,1))
    #plt.figure(3)
    # fromFile = Graph.from_csv("FacebookData/Data_Facebook.csv")
    # draw(fromFile.kruskal()[0].asNxGraph(), with_labels=True)
    plt.show()

