import numpy as np
arr = np.arange(12)        # [0, 1, ..., 11]
arr.reshape(3, 4)          # reshape to 3x4

# Flatten
arr.ravel()                # 1D view
arr.flatten()              # 1D copy

# Broadcasting
a = np.array([[1], [2], [3]])  # shape (3,1)
b = np.array([10, 20, 30])     # shape (3,)
a + b    # [[11,21,31],[12,22,32],[13,23,33]]
