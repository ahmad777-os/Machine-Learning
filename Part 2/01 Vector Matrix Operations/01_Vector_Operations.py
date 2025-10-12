import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------
# 1. Define vectors
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

# -----------------------------------------------------------------------
# 2. Vector operations
addition = u + v
subtraction = u - v
multiplication = u * v   # element-wise multiplication

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Element-wise Multiplication:", multiplication)

# -----------------------------------------------------------------------
# 3. Scalar multiplication
k = 3
scalar_mul = k * u
print("Scalar Multiplication:", scalar_mul)

# -----------------------------------------------------------------------
# 4. Angle between two vectors
dot_product = np.dot(u, v)
magnitude_u = np.linalg.norm(u)
magnitude_v = np.linalg.norm(v)

cos_theta = dot_product / (magnitude_u * magnitude_v)
theta_radians = np.arccos(cos_theta)
theta_degrees = np.degrees(theta_radians)

print("Angle (radians):", theta_radians)
print("Angle (degrees):", theta_degrees)

# -----------------------------------------------------------------------
# 5. Cross product (only for 3D vectors)
cross = np.cross(u, v)
print("Cross Product:", cross)

# -----------------------------------------------------------------------
# 6. Projection of u onto v (2D case)
u_2d = np.array([3, 4])
v_2d = np.array([1, 2])

projection = (np.dot(u_2d, v_2d) / np.dot(v_2d, v_2d)) * v_2d
print("Projection of u on v:", projection)

# -----------------------------------------------------------------------
# 7. (Optional) Vector visualization with quiver
# plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
# - X, Y → starting points of the arrow (vector tail)
# - U, V → components of the vector (direction)
# - angles='xy' → ensures correct orientation in x-y plane
# - scale_units='xy' → length matches coordinates
# - scale=1 → no auto-scaling (true magnitude shown)
