# 2. pivot() – Pivoting
# Turns rows into columns. It's the reverse of melt.
# Syntax
# df.pivot(index='id', columns='subject', value='score')
import pandas as pd
df = pd.DataFrame({
    'id': [1, 1, 2, 2],
    'subject': ['math', 'science', 'math', 'science'],
    'score': [85, 80, 90, 95]
})

pivoted = df.pivot(index='id', columns='subject', values='score')
