import pandas as pd
df = pd.read_csv('pokemon.csv')

print(df.isnull().sum())
print("--------------------------------------------------------------------------------------------------------")
# c. dropna()
# Used to remove rows (or columns) with missing values.
df.dropna(inplace=True)  # Drops rows with any NaN
df.dropna(axis=1)        # Drops columns with any NaN
