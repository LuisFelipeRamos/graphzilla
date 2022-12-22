from __future__ import annotations

import numpy as np
import numpy.typing as npt

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

from collections import deque
from graphzilla.classes import *

""" Performes a depth first search in a graph, directed or undirected, and returns the nodes in order of visit.
By default, it uses a iterative approach. A recursive approach is yet to be implemented.
It does a preorder traversal in the graph.Inorder and Postorder are yet to be implemented.
The starting nodes is, by default, node 0. You can change it in the parameter starting_node """
def depth_first_search_nodes(graph, starting_node: int = 0, mode: str = "preorder"):
    visited: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_)
    stack: deque = deque()
    stack.append(starting_node)
    order_of_visit: list[int] = []
    while len(stack) > 0:
        curr_node: int = stack.pop()
        if not visited[curr_node]:
            visited[curr_node] = 1
            order_of_visit.append(curr_node)
            for neighboor in graph.neighboors(curr_node):
                if not visited[neighboor]:
                    stack.append(neighboor)
    return order_of_visit

""" Performes a depth first search in a graph, directed or undirected, and returns de dfs tree.
It does a preorder traversal in the graph. Inorder and Postorder are yet to be implemented.
The starting nodes is, by default, node 0. You can change it in the parameter starting_node """
def depth_first_search_tree(graph, starting_node: int = 0):
    visited: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_)
    stack: deque = deque()
    stack.append((starting_node, None))
    dfs_tree: Graph = Graph(nodes = graph.nodes)
    while len(stack) > 0:
        curr_node, prev_node = stack.pop()
        if not visited[curr_node]:
            visited[curr_node] = 1
            if prev_node is not None:
                dfs_tree.add_edge((curr_node, prev_node))
            for neighboor in graph.neighboors(curr_node):
                if not visited[neighboor]:
                    stack.append((neighboor, curr_node))
    return dfs_tree

""" Performes a breadth first search in a graph, directed or undirected.
Returns a NxN matrix with the layers oh each node in respect to the starting node (for
unweighted graphs, it can be used to compute shortest path between starting node and every other node).
By default, it uses a iterative approach. A recursive approach is yet to be implemented.
The starting nodes is, by default, node 0. You can change it in the parameter starting_node """
def breadth_first_search(graph, starting_node: int = 0):
    visited: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_)
    layers: NDArrayInt = np.zeros((graph.number_of_nodes, graph.number_of_nodes), dtype = np.int_)
    stack: deque = deque()
    stack.append((starting_node,None))
    while len(stack) > 0:
        curr_node, prev_node = stack.pop()
        if prev_node is not None:
            curr_dist: int = layers[prev_node][curr_node]
        else:
            curr_dist: int = 0
        if not visited[curr_node]:
            visited[curr_node] = 1
            for neighboor in graph.neighboors(curr_node):
                if not visited[neighboor]:
                    stack.append((neighboor, curr_node))
                    layers[prev_node][curr_node] = curr_dist + 1
    return layers
