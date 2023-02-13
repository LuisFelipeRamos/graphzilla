from __future__ import annotations

import numpy as np
import numpy.typing as npt

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

from heapq import *
from graphzilla.classes import *

""" Computes the minimum distance from starting node to every other node in the graph, using
Djikstra's algorithm. It uses a priority queue to order paths. 
TODO: use indexed priority queue. """
def dijkstra(graph: Graph, starting_node: int = 0):
    visited: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_)
    dist: NDArrayFloat = np.ones(graph.number_of_nodes, dtype = np.int_) * np.inf
    prev: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_) # should return prev to
    pq = [(0, starting_node)] # Heap takes a tuple of (dist, node)
    heapify(pq)
    while len(pq) > 0:
        curr_dist, curr_node = heappop(pq)
        if not visited[curr_node]:
            dist[curr_node] = curr_dist
            visited[curr_node] = 1
        for neighbor in graph.neighbors(curr_node):
            if not visited[neighbor]:
                new_dist = graph.get_weight(curr_node, neighbor) + dist[curr_node]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(pq, (new_dist, neighbor))
    return dist

def bellman_ford():
    pass

""" Computes the all pairs shortest paths using floyd warshall algorithm. """
def floyd_warshall(graph: Graph):
    number_of_nodes: np.int_ = graph.number_of_nodes
    shortest_paths: NDArrayFloat = np.copy(graph.adjacency_matrix).astype(np.float_)
    shortest_paths[shortest_paths == 0] = np.inf
    np.fill_diagonal(shortest_paths, 0)
    for k in range(number_of_nodes):
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                shortest_paths[i, j] = min(shortest_paths[i, j], shortest_paths[i, k] + shortest_paths[k, j])
    return shortest_paths
