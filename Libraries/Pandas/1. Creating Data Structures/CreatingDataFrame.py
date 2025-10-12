# From a List of Dictionaries:
import pandas as pd
data = [
    {'Name': 'Ahmad', 'Age': 20},
    {'Name': 'Tariq', 'Age': 21},
]

df = pd.DataFrame(data)

print(df)

# From Nested Lists:

data = [
    ['Ahmad', 20],
    ['Tariq', 21]
]

df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)

#  From a Dictionary of Lists:

data = {
    'Name': ['Ahmad', 'Tariq'],
    'Age': [20, 21]
}

df = pd.DataFrame(data)

print(df)
