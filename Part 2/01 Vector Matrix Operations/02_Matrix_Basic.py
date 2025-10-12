import numpy as np

# 1. Scalars, Vectors, Matrices
scalar = 5
print("Scalar:", scalar)

vector = np.array([1, 2, 3])
print("Vector:", vector)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Matrix:\n", matrix)

# 2. Shape of a Matrix
print("Shape of vector:", vector.shape)
print("Shape of matrix:", matrix.shape)

# 3. Different Types of Matrices
square_matrix = np.array([
    [1, 2],
    [3, 4]
])

zero_matrix = np.zeros((3, 3))
identity_matrix = np.eye(3)
diagonal_matrix = np.diag([1, 2, 3])

print("Square Matrix:\n", square_matrix)
print("Zero Matrix:\n", zero_matrix)
print("Identity Matrix:\n", identity_matrix)
print("Diagonal Matrix:\n", diagonal_matrix)

# 4. Transpose of a Matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

transpose_A = A.T
print("Original Matrix:\n", A)
print("Transpose:\n", transpose_A)

# 5. A Matrix with Random Values
random_matrix  = np.random.rand(3,3)
print("Random Matrix : ", random_matrix)

random_matrix_int = np.random.randint(100, size=(4, 5))
print("Random Integer Matrix : ", random_matrix_int)

matrix_value_one = np.ones((2,3), dtype=int)
print("Matrix with 1 : ", matrix_value_one)