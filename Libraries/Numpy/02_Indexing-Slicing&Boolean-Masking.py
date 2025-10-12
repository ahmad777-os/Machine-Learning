import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr)
# Access element
print(arr[0, 1] )   # 20

# Slice rows & cols
print(arr[0:2, 1:]) # [[20, 30], [50, 60]]

# Boolean indexing
mask = arr > 30
print(arr[mask] )   # [40, 50, 60]
