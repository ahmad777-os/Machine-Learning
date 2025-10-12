import pandas as pd

dataframe = pd.read_csv('pokemon.csv')
print("Whole data set")
print(dataframe)
print("Head of dataset")
print(dataframe.head(4)) # printing top 3 rows
print("Tail of dataset")
print(dataframe.tail(4)) # printing bottom 3 rows