# 1. melt() – Unpivoting
# Turns columns into rows. Useful when you want to normalize data for analysis.
# Syntax
# pd.melt(df, id_vars=['id'], value_vars=['col1', 'col2'])
import pandas as pd

df = pd.DataFrame({
    'id': [1, 2],
    'math': [85, 90],
    'science': [80, 95]
})

melted = pd.melt(df, id_vars=['id'], value_vars=['math', 'science'])
print(melted)