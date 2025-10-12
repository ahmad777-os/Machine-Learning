import pandas as pd
df = pd.read_csv('pokemon.csv')
print(df.columns)
# Get only the 'Name' column
print(df['name'].head())

# Get multiple columns
print(df[['name', 'defense', 'type1']].head())

# Get row with index 3
print(df.loc[3])

# Get the first row using iloc
print(df.iloc[0])

# Slicing first 10 rows
print(df[0:10])

# Filtering all Pokémon with Speed > 120
print(df[df['speed'] > 120])

# Filtering Water-type Pokémon
print(df[df['type1'] == 'Water'])

