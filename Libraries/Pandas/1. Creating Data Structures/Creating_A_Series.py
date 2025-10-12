# from a List

import pandas as pd
data = [10,20,30,40]
s = pd.Series(data)
print(s)

# from a dictionary

data_dic = {'a':100, 'b':200, 'c': 300}
s_dic = pd.Series(data)
print(s_dic)

# from a numpy array

import numpy as np
arr = np.array([5,10,15])
s_np = pd.Series(arr)
print(s_np)