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
        nodes: list[int] = np.arange(5)
        edges: list[tuple[int]] = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 3), (2, 3), (3, 4)]
        graph: Graph = Graph(nodes, edges)
        dfs_preorder_nodes: list[int] = depth_first_search_nodes(graph)
        assert dfs_preorder_nodes == [0, 4, 3, 2, 1]

    def test_dfs_tree_1(self):
        nodes: list[int] = np.arange(5)
        edges: list[tuple[int]] =  [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 4)]
        graph: Graph = Graph(nodes, edges)
        dfs_tree: Graph = depth_first_search_tree(graph)
        expected_edges: list[tuple[int]] = [(0, 3), (3, 4), (3, 2), (3, 1)]
        expected_tree: Graph = Graph(nodes, expected_edges)
        assert np.all(expected_tree.adjacency_matrix == dfs_tree.adjacency_matrix)
        
class TestMinimumSpanningTree:

    def test_prim_1(self):
        nodes: list[int] = np.arange(9)
        edges: list[tuple[tuple[int]]] = [((0, 1), 4), ((0, 7), 8), ((1, 7), 11), ((1, 2), 8), ((2, 3), 7), ((2, 8), 2),
        ((2, 5), 4), ((8, 7), 7), ((8, 6), 6), ((7, 6), 1), ((6, 5), 2), ((3, 5), 14), ((3, 4), 9), ((4, 5), 10)]
        graph: Graph = Graph(nodes, edges, weighted=True)
        mst: Graph = prim(graph)
        expected_edges: list[tuple[tuple[int]]] = [((0, 1), 4), ((0, 7), 8), ((2, 3), 7), ((2, 8), 2),
        ((2, 5), 4), ((7, 6), 1), ((6, 5), 2), ((3, 4), 9)]
        expected_mst: Graph = Graph(nodes, expected_edges, weighted=True)
        assert np.all(mst.adjacency_matrix == expected_mst.adjacency_matrix)
    
    def test_kruskal_1(self):
        nodes: list[int] = np.arange(9)
        edges: list[tuple[tuple[int]]] = [((0, 1), 4), ((0, 7), 8), ((1, 7), 11), ((1, 2), 8), ((2, 3), 7), ((2, 8), 2),
        ((2, 5), 4), ((8, 7), 7), ((8, 6), 6), ((7, 6), 1), ((6, 5), 2), ((3, 5), 14), ((3, 4), 9), ((4, 5), 10)]
        graph: Graph = Graph(nodes, edges, weighted=True)
        mst: Graph = kruskal(graph)
        expected_edges: list[tuple[tuple[int]]] = [((0, 1), 4), ((0, 7), 8), ((2, 3), 7), ((2, 8), 2),
        ((2, 5), 4), ((7, 6), 1), ((6, 5), 2), ((3, 4), 9)]
        expected_mst: Graph = Graph(nodes, expected_edges, weighted=True)
        assert np.all(mst.adjacency_matrix == expected_mst.adjacency_matrix)