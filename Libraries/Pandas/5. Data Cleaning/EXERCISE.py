import pandas as pd

# Load data
df = pd.read_csv('pokemon.csv')

print('Full Dataset')
print(df)

print("-----------------------------------------------------------------------------------------------------------")

# Check missing values BEFORE cleaning
print("Missing Values Before Cleaning")
print(df.isnull().sum())

print("-----------------------------------------------------------------------------------------------------------")

# Check specific column data types
print("Specific Column Data Types")
print("height_m:", df['height_m'].dtype)
print("percentage_male:", df['percentage_male'].dtype)
print("type2:", df['type2'].dtype)
print("weight_kg:", df['weight_kg'].dtype)

print("-----------------------------------------------------------------------------------------------------------")

# Fill numeric columns
df['height_m'].fillna(df['height_m'].mean(), inplace=True)
df['weight_kg'].fillna(df['weight_kg'].mean(), inplace=True)
df['percentage_male'].fillna(df['percentage_male'].mean(), inplace=True)

# Fill categorical column
df['type2'].fillna('None', inplace=True)

# Check missing values AFTER filling
print("Missing Values After Cleaning")
print(df.isnull().sum())
