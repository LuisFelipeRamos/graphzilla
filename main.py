from graphzilla.classes import *
from graphzilla.functions import *

import networkx as nx
import matplotlib.pyplot as plt

def main():

    nodes: list[int] = np.arange(9)
    edges: list[tuple[tuple[int]]] = [((0, 1), 4), ((0, 7), 8), ((1, 7), 11), ((1, 2), 8), ((2, 3), 7), ((2, 8), 2),
        ((2, 5), 4), ((8, 7), 7), ((8, 6), 6), ((7, 6), 1), ((6, 5), 2), ((3, 5), 14), ((3, 4), 9), ((4, 5), 10)]

    nodes = np.arange(5)
    edges = [((0, 1), 4), ((0, 2), 1), ((1, 2), 2), ((1, 3), 1), ((2, 3), 5), ((3, 4), 3)]
    grafo = Graph(nodes, edges)

  

    

if __name__ == "__main__":
    main()