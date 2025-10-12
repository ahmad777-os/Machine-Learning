import numpy as np

# Define matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matrix addition
addition = A + B
print("A + B =\n", addition)

# Matrix subtraction
subtraction = A - B
print("A - B =\n", subtraction)

# Scalar multiplication
scalar_mult = 2 * A
print("2 * A =\n", scalar_mult)

# Matrix multiplication (dot product)
multiplication = np.dot(A, B)   # or A @ B
print("A x B =\n", multiplication)

# if the shape is not same then we dont perform operations