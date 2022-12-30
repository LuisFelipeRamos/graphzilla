import numpy as np
import numpy.typing as npt

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

import graphblas as gb
import networkx as nx
from scipy.sparse import *
from scipy.sparse.csgraph import floyd_warshall

graph = random(5, 5, density=0.25, data_rvs=np.ones).astype(np.int_)

gb_graph = gb.io.from_scipy_sparse(graph)


C = gb.semiring.min_plus(gb_graph @ gb_graph)
print(C)

def gb_shortest_paths(gb_graph) -> NDArrayFloat:
    shortest_paths: NDArrayFloat = np.zeros(gb_graph.shape)


# print(floyd_warshall(graph.todense()))
