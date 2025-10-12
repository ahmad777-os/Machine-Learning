# 🔸 concat() – Stacking DataFrames Vertically or Horizontally
# Use Case: When you want to combine multiple DataFrames along rows (vertical) or columns (horizontal).
import pandas as pd
df1 = pd.DataFrame({
    'ID':[1,2],
    'Name':['Ahmad', 'Ali']
})

df2 = pd.DataFrame({
    'ID':[3, 4],
    'Name':['Akbar', 'Junaid']
})

result = pd.concat([df1, df2])
print("Stacking DataFrame Verticaly")
print(result)
print("===================================================================")
# Horizontally Side by Side 

df3 = pd.DataFrame({
    'Age':[23, 30]
})
df4 = pd.DataFrame({
    'City':['Lahore', 'Karachi']
})
print("Stacking Data Horizontally")
print(pd.concat([df3, df4], axis = 1))
print("===================================================================")

# 🔸 merge() – SQL-style Joins
# Use Case: When you want to combine DataFrames based on one or more common columns.
df5 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Ali', 'Ahmed', 'Ahsan']
})

df6 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Marks': [88, 76, 90]
})
# Inner Join (Only matching IDs)
print("Merge inner Join")
print(pd.merge(df5, df6, on='ID', how='inner'))
print("===================================================================")
# Left Join (All from df1 + match from df2)
print("Merge Left Join")
print(pd.merge(df5, df6, on='ID', how='left'))
print("===================================================================")
# Right Join (All from df2 + match from df1)
print("Merge Right Join")
print(pd.merge(df5, df6, on='ID', how='right'))
print("===================================================================")
# Outer Join (All data from both, NaN where missing)
print("Merge Outer Join")
print(pd.merge(df5, df6, on='ID', how='outer'))
print("===================================================================")
