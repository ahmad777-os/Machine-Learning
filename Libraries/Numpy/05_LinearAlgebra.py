import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.dot(A, B)            # Matrix multiplication
A @ B                   # Same as dot()
np.linalg.inv(A)        # Inverse
np.linalg.det(A)        # Determinant
np.linalg.eig(A)        # Eigenvalues & vectors
