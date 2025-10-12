import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]])

np.mean(data)           # Mean of all
np.mean(data, axis=0)   # Mean per column
np.std(data)            # Standard deviation
np.min(data), np.max(data)
np.sum(data, axis=1)    # Sum per row
