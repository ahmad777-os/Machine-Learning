import numpy as np

# 1D Array
a = np.array([1, 2, 3])

# 2D Array
b = np.array([[1, 2], [3, 4]])

# Special arrays
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
rand = np.random.rand(2, 3)     # Uniform random [0,1)
randn = np.random.randn(2, 3)   # Normal distribution
eye = np.eye(3)                 # Identity matrix

# inspecting arrays
b.shape       # (rows, cols)
b.ndim        # number of dimensions
b.size        # total elements
b.dtype       # data type
