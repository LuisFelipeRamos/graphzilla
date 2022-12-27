import numpy as np
import numpy.typing as npt

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

from ..classes import *

""" Creates a graph from it's adjacency matrix. """
def from_adjacency_matrix(adjacency_matrix: NDArrayFloat, weighted: bool = False, directed: bool = False):
    pass
