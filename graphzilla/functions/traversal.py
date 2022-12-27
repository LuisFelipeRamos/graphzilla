from __future__ import annotations

import numpy as np
import numpy.typing as npt

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

from collections import deque
from graphzilla.classes import *

""" Performes a depth first search in a graph, directed or undirected, and returns the nodes in order of visit.
By default, it uses a iterative approach. A recursive approach is yet to be implemented.
The starting nodes is, by default, node 0. You can change it in the parameter starting_node """
def depth_first_search_nodes(graph: Graph, starting_node: int = 0):
    visited: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_)
    stack: deque = deque()
    stack.append(starting_node)
    order_of_visit: list[int] = []
    while len(stack) > 0:
        curr_node: int = stack.pop()
        if not visited[curr_node]:
            visited[curr_node] = 1
            order_of_visit.append(curr_node)
            for neighbor in graph.neighbors(curr_node):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return order_of_visit

""" Performes a depth first search in a graph, directed or undirected, and returns de dfs tree.
The starting nodes is, by default, node 0. You can change it in the parameter starting_node """
def depth_first_search_tree(graph: Graph, starting_node: int = 0):
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
            for neighbor in graph.neighbors(curr_node):
                if not visited[neighbor]:
                    stack.append((neighbor, curr_node))
    return dfs_tree

""" Performes a breadth first search in a graph, directed or undirected.
Returns a array matrix with the layers oh each node in respect to the starting node (for
unweighted graphs, it can be used to compute shortest path between starting node and every other node).
By default, it uses a iterative approach. A recursive approach is yet to be implemented.
The starting nodes is, by default, node 0. You can change it in the parameter starting_node. 
OBS: the layer value -1 means that there is no path between the starting node and the node with layer value -1."""
def breadth_first_search_layers(graph: Graph, starting_node: int = 0):
    visited: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_)
    visited[starting_node] = 1
    layers: NDArrayInt = np.ones(graph.number_of_nodes, dtype = np.int_) * -1
    layers[starting_node] = 0
    queue: deque = deque()
    queue.append(starting_node)
    while len(queue) > 0:
        curr_node = queue.popleft()
        for neighbor in graph.neighbors(curr_node):
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)
                layers[neighbor] = layers[curr_node] + 1
    return layers

""" Performes a breadth first search in a graph, directed or undirected.
Returns the bfs tree of the graph.
By default, it uses a iterative approach. A recursive approach is yet to be implemented.
The starting nodes is, by default, node 0. You can change it in the parameter starting_node. 
"""
def breadth_first_search_tree(graph: Graph, starting_node: int = 0):
    visited: NDArrayInt = np.zeros(graph.number_of_nodes, dtype = np.int_)
    visited[starting_node] = 1
    bfs_tree: Graph = Graph(nodes = graph.nodes)
    queue: deque = deque()
    queue.append(starting_node)
    while len(queue) > 0:
        curr_node = queue.popleft()
        for neighbor in graph.neighbors(curr_node):
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)
                bfs_tree.add_edge((curr_node, neighbor))
    return bfs_tree