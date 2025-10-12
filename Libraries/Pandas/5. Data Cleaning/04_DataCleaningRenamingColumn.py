import pandas as pd

# Load CSV
df = pd.read_csv('pokemon.csv')

# Display original column names
print(df.columns)

# Rename columns
df.rename(columns={'name': 'Full_Name', 'abilities': 'Abilities'}, inplace=True)

# Check updated columns
print(df.columns)
print("---------------------------------------------")

# If you want to rename Full_Name to Name, do it here
df.rename(columns={'Full_Name': 'Name'}, inplace=True)

# Now 'Name' column exists, and you can use it
print(df[['Name', 'Abilities', 'speed']].head())

# Safe conversions
df['Name'] = df['Name'].astype(str)  # ✅ Safe
df['Abilities'] = df['Abilities'].astype(str)  # Since it's a list-like string, float conversion is invalid
df['speed'] = df['speed'].astype(str)  # ✅ Safe

# Final data types
print(df.dtypes)
