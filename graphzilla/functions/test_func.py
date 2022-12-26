import pytest
""" This file contains test classes for every st of functions defined
in this directory. The library pytest is used for the tests. """

from . import *

class TestDepthFirstSearch:

    def test_dfs_preorder_1(self):

        nodes: list[int] = np.arange(5)
        edges: list[tuple[int]] = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 4)]
        graph: Graph = Graph(nodes, edges)
        dfs_preorder_nodes: list[int] = depth_first_search_nodes(graph)
        assert dfs_preorder_nodes == [0, 3, 4, 2, 1]
    
    def test_dfs_preorder_2(self):
        nodes: list[int] = np.arange(6)
        edges: list[tuple[int]] = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 3), (2, 3), (3, 4)]
        graph: Graph = Graph(nodes, edges)
        dfs_preorder_nodes: list[int] = depth_first_search_nodes(graph)
        assert dfs_preorder_nodes == [0, 4, 3, 2, 1]

    def test_dfs_tree_1(self):
        nodes: list[int] = np.arange(6)
        edges: list[tuple[int]] =  [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 4)]
        graph: Graph = Graph(nodes, edges)
        dfs_tree: Graph = depth_first_search_tree(graph)
        expected_edges: list[tuple[int]] = [(0, 3), (3, 4), (3, 2), (3, 1)]
        expected_tree: Graph = Graph(nodes, expected_edges)
        assert np.all(expected_tree.adjacency_matrix == dfs_tree.adjacency_matrix)
        