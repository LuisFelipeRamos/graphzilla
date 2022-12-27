import numpy as np
import numpy.typing as npt

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

""" Represents an undirected graph """
class Graph:

    """ Instance initializer for the class. Receives a list of nodes, that must be integer values from 0 to the
        number of nodes in the graph, and a list of edges, that must be a list of of binary tuples. The tuples 
        must represent the two nodes that are connected by that edge. 
        If the lists are empty, then and empty graph is created.
        If the argument weighted is true (by default, it is false), the initializer will check for an extra value 
        in the edges input data, which will be the weight 
        of such edge. The instances are created in the form of an adjacency matrix."""

    def __init__(self, nodes: list[int] = [], edges: list[tuple[int]] = [], weighted: bool = False):
        self.nodes: list[int] = nodes
        self.edges: list[tuple[int]] = edges
        self.weighted: bool = weighted
        self.number_of_nodes: int = len(self.nodes)
        self.number_of_edges: int = len(self.edges)
        self.adjacency_matrix: NDArrayInt = np.zeros((self.number_of_nodes, self.number_of_nodes), dtype = np.int_)
        if not self.weighted:
            for edge in edges:
                self.adjacency_matrix[edge] = 1
                self.adjacency_matrix[tuple(reversed(edge))] = 1
        else:
            for edge in self.edges:
                self.adjacency_matrix[edge[0]] = edge[1]
                self.adjacency_matrix[tuple(reversed(edge[0]))] = edge[1]
        
    """ Get neighboors of node in graph. """
    def neighbors(self, node: int) -> NDArrayInt:
        return np.where(self.adjacency_matrix[node] != 0)[0]

    """ Add edge to graph. """
    def add_edge(self, edge: tuple[int]):
        if not self.weighted:
            self.adjacency_matrix[edge] = 1
            self.adjacency_matrix[tuple(reversed(edge))] = 1
        else:
            self.adjacency_matrix[edge[0]] = edge[1]
            self.adjacency_matrix[tuple(reversed(edge[0]))] = edge[1]
        self.edges.append(edge)
        self.number_of_edges += 1
    
    """ Get weight between nodes S and T """
    def get_weight(self, s: int, t: int):
        if not self.weighted:
            return 1
        return self.adjacency_matrix[s, t]

    def __repr__(self):
        return f"Graph with {self.number_of_nodes} nodes and {self.number_of_edges} edges"
