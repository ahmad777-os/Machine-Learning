# ✅ 2. Aggregation Functions
import pandas as pd

data = {
    'City': ['Lahore', 'Karachi', 'Lahore', 'Islamabad', 'Karachi'],
    'Product': ['A', 'A', 'B', 'A', 'B'],
    'Sales': [200, 300, 250, 400, 150],
    'Quantity': [2, 3, 5, 4, 1]
}

df = pd.DataFrame(data)
print(df)
print("----------------------------------")
# ➤ sum() – total

print(df.groupby('City')['Sales'].sum())
print("----------------------------------")
# ➤ mean() – average

print(df.groupby('Product')['Sales'].mean())
print("----------------------------------")
# ➤ count() – number of entries

print(df.groupby('City')['Sales'].count())
print("----------------------------------")
# ➤ agg() – multiple aggregations

print(df.groupby('City')['Sales'].agg(['sum', 'mean', 'count']))

# ✅ 3. Multi-level Grouping

grouped = df.groupby(['City', 'Product']).agg({'Sales': 'sum', 'Quantity': 'mean'})
print(grouped)
# You can even use .loc[] to access:
grouped.loc['Lahore']

# ✅ 4. Pivot Table

pd.pivot_table(df, index='City', columns='Product', values='Sales', aggfunc='sum')
