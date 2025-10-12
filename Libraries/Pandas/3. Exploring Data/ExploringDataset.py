import pandas as pd

df = pd.read_csv("pokemon.csv")

print(df)

df.head()       # First 5 rows
df.head(10)     # First 10 rows

df.tail()       # Last 5 rows
df.tail(3)      # Last 3 rows

df.info() # Gives a summary: column names, non-null counts, and data types.

df.describe() # Gives statistical summary of numeric columns (mean, std, min, max, etc.)

print(df.shape)   # (rows, columns)

print(df.columns)  # Returns a list of column names

print(df.index)   #   Shows the index (row labels) of the DataFrame:

print(df.dtypes)  #  Tells you the data type of each column





