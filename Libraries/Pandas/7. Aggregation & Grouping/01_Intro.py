import pandas as pd

data = {
    'City': ['Lahore', 'Karachi', 'Lahore', 'Islamabad', 'Karachi'],
    'Product': ['A', 'A', 'B', 'A', 'B'],
    'Sales': [200, 300, 250, 400, 150],
    'Quantity': [2, 3, 5, 4, 1]
}

df = pd.DataFrame(data)
print(df)
# ✅ 1. groupby()
# ➤ Group by one column
print(df.groupby('City')['Sales'].sum())
# This tells total sales per city.
# ➤ Group by two columns
print("---------------------------------------------------")
print(df.groupby(['City', 'Product'])['Sales'].sum())
# This tells total sales for each product in each city.

