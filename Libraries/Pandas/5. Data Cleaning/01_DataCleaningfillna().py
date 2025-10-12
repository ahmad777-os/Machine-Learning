import pandas as pd
dataframe = pd.read_csv('pokemon.csv')
print(dataframe)
print("------------------------------------------------------")
# check which values are missing
print("Checking Null Values")
print(dataframe.isnull().sum())

print("------------------------------------------------------")
# b. fillna()
# Fill missing numeric values with mean
dataframe['height_m'].fillna(dataframe['height_m'].mean())
dataframe['weight_kg'].fillna(dataframe['weight_kg'].mean())
dataframe['percentage_male'].fillna(dataframe['percentage_male'].mean())

# Fill missing categorical values
dataframe['type2'].fillna('None')

# Double-check that no missing values remain
print("\n✅ After Cleaning:")
print(dataframe.isnull().sum())


print(dataframe.to_csv("pokemon_cleaned.csv", index = False))

