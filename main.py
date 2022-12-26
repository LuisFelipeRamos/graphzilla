from graphzilla.classes import *
from graphzilla.functions import *

import networkx as nx
import matplotlib.pyplot as plt

def main():
    nodes: list[int] = np.arange(9)
    edges: list[tuple[tuple[int]]] = [((0, 1), 4), ((0, 7), 8), ((1, 7), 11), ((1, 2), 8), ((2, 3), 7), ((2, 8), 2),
        ((2, 5), 4), ((8, 7), 7), ((8, 6), 6), ((7, 6), 1), ((6, 5), 2), ((3, 5), 14), ((3, 4), 9), ((4, 5), 10)]
    grafo = Graph(nodes, edges, weighted=True)
    mst = kruskal(grafo)
    

    g = nx.Graph(mst.adjacency_matrix)
    nx.draw_networkx(g)
    plt.show()

if __name__ == "__main__":
    main()