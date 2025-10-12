import pandas as pd
df = pd.read_csv('pokemon.csv')

print(df.duplicated())
print("-----------------------------------------------------------------------------")

# b. drop_duplicates()
# Used to remove duplicated rows.

print(df.drop_duplicates(inplace=True))
print("-----------------------------------------------------------------------------")
# you can also check a duplicate in a specific column 
print(df.drop_duplicates(subset='name', keep='first', inplace=True))
print("-----------------------------------------------------------------------------")