from graphzilla.classes import *
from graphzilla.functions import *

def main():
    nodes = [0,1,2,3,4]
    edges = [(0,1),(0,3),(1,2),(1,3),(1,4),(2,4),(3,4)]
    grafo = Graph(nodes, edges)
    print(depth_first_search_tree(grafo).adjacency_matrix)

if __name__ == "__main__":
    main()