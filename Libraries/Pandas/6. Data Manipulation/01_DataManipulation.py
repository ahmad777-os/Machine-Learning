import pandas as pd

data = {
    'Name': ['Ali', 'Zara', 'Ahmed', 'Sara'],
    'Age': [25, 30, 22, 27],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore']
}

df = pd.DataFrame(data)

df['Country'] = 'Pakistan'
df['Age in 5 Years'] = df['Age'] + 5
df['Double Age'] = df['Age'].apply(lambda x: x * 2)
df['Short Name'] = df['Name'].map(lambda x: x[0])
df['City'] = df['City'].replace('Lahore', 'LHR')
df['Name_upper'] = df['Name'].str.upper()
df['From_Lahore'] = df['City'].str.contains('LHR')

print(df)
