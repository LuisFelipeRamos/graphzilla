from __future__ import annotations

import numpy as np
import numpy.typing as npt

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

from heapq import *
from graphzilla.classes import *

""" Computes a minimum spanning tree of the graph using Prim's algorithm.
By default, it starts at node 0. """
def prim(graph: Graph, starting_node: np.int_ = 0):
    mst: Graph = Graph(nodes = graph.nodes, weighted=True)
    visited: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_)
    visited[starting_node] = 1
    pq = [(graph.get_weight(starting_node, neighboor), (starting_node, neighboor)) for neighboor in graph.neighboors(starting_node)]
    heapify(pq)
    while mst.number_of_edges < mst.number_of_nodes - 1:
        curr_edge: int = heappop(pq)
        node_s: int = curr_edge[1][0]
        node_t: int = curr_edge[1][1]
        if not visited[node_s] or not visited[node_t]:
            mst.add_edge((curr_edge[1], curr_edge[0]))
            visited[node_s] = 1
            visited[node_t] = 1
            for edge in [(graph.get_weight(node_t, neighboor), (node_t, neighboor)) for neighboor in graph.neighboors(node_t) if not visited[neighboor]]:
                heappush(pq, edge)
    return mst