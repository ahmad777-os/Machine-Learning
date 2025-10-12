import pandas as pd
df1 = pd.DataFrame({
    'Name':['Ahmad', 'Ali']
}, index=[1,2])

df2 = pd.DataFrame({
    'Name':['Akbar', 'Junaid']
}, index=[3, 4])

# Default is Left Join
df1.join(df2)
# You can also change to how='outer':
df1.join(df2, how='outer')

