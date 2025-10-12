import pandas as pd

df = pd.read_csv('pokemon.csv')
print(df)


# top rows
print("TOP ROWS")
print(df.head())
print(df.head(15))


# down rows
print("DOWN ROWS")
print(df.tail())
print(df.tail(10))

# getting its information
print("GETTING INFORMATION")
print(df.info())

# getting its statictical measures 
print("GETTING ITS STASTISTICALS MEASURES")
print(df.describe())

print("SHAPE COLUMN INDEX")
print("SHAPE")
print(df.shape)
print("COLUMN")
print(df.columns)
print("INDEX")
print(df.index)
print("DATATYPES")
print(df.dtypes)


# getting abilities pokemon
ability = df[df["abilities"] == True]
ability.to_csv("legendry_pokemon", index = False)