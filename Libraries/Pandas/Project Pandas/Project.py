import pandas as pd
df =pd.read_csv('Titanic-Dataset.csv')
print("Full Dataset")
# print(df)
print("========================================================================================================")

# Exploring Dataset 
print("Dataset Head")
print(df.head())
print("========================================================================================================")
print("Dataset Tail")
print(df.tail())
print("========================================================================================================")
print("Dataset Columns")
print(df.columns)
print("========================================================================================================")
print("Dataframe Shape")
print(df.shape)
print("========================================================================================================")
print("Dataset Datatypes")
print(df.dtypes)
print("========================================================================================================")
print("Describe Dataframe")
print(df.describe())
print("========================================================================================================")
print("Dataset Info")
print(df.info())

print("========================================================================================================")
print("========================================================================================================")
print("========================================================================================================")

# Cleaning Dataset

print("Checking Null Values")
# print(df.isnull())
print(df.isnull().sum())
print("========================================================================================================")
print("Filling Numeric columns")
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("Filling Object columns")
df['Cabin'] = df['Cabin'].fillna('Missing')
df['Embarked'] = df['Embarked'].fillna('Missing')

print("Cleaned Dataset")
print(df)
print(df.isnull().sum())

print("========================================================================================================")
print("========================================================================================================")
print("========================================================================================================")

# Feature Engineering

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

print(df.columns)

print("========================================================================================================")
print("========================================================================================================")
print("========================================================================================================")

# Data Analysis

print("How many passengers survived?")
print(df['Survived'].sum())
survival_by_gender = df.groupby('Sex')['Survived'].mean()
print("Survival Rate by Gender:")
print(survival_by_gender)

print("How many pclass Passengers Survived?")
survival_by_pclass  = df.groupby('Pclass')['Survived'].mean()
print("Survival rate by Pclass")
print(survival_by_pclass)