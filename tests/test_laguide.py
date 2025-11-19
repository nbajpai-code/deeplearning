import numpy as np
from laguide import DotProduct

def test_dot_product():
    U = np.array([[1], [2], [3]])
    V = np.array([[4], [5], [6]])
    assert DotProduct(U, V) == 32.0
