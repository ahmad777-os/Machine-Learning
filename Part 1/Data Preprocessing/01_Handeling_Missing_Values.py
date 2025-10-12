import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Placement_Dataset.csv')

print(df.head())
print(df.shape)
print(df.isnull().sum())

# | Skew Type        | Tail Direction | Mean vs Median | Best for Filling Missing |
# | ---------------- | -------------- | -------------- | ------------------------ |
# | **Right-skewed** | Right          | Mean > Median  | Median                   |
# | **Left-skewed**  | Left           | Mean < Median  | Median                   |
# | **Normal**       | Balanced       | Mean ≈ Median  | Mean                     |

# Plot distribution of salary
sns.histplot(df['salary'], kde=True)  
plt.show()

# Fill missing values with median
df['salary'].fillna(df['salary'].median(), inplace=True)
print(df.isnull().sum())


# # droping missing values
# dataset = pd.read_csv('Placement_Dataset.csv')
# print(dataset.head())
# dataset = dataset.dropna(how = 'any')
# dataset.isnull().sum()
# dataset.shape