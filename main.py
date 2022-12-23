from graphzilla.classes import *
from graphzilla.functions import *

import networkx as nx
import matplotlib.pyplot as plt

def main():
    nodes = [0,1,2,3,4]
    edges = [((0,1), 4),((0,3), 17),((1,2), 8),((1,3), 2),((1,4), 5), ((2,4), 12), ((3, 2), 9)]
    grafo = Graph(nodes, edges, weighted=True)
    mst = prim(grafo)
    
    g = nx.Graph(mst.adjacency_matrix)
    nx.draw_networkx(g)
    plt.show()

if __name__ == "__main__":
    main()