import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset
dataset = pd.read_csv('diabetes.csv')

# Preview dataset
print("\nFirst 5 rows of the dataset:")
print(dataset.head())

# Dataset shape (rows, columns)
print("\nDataset shape:", dataset.shape)

# Statistical summary
print("\nDataset description:")
print(dataset.describe())

# Class distribution in 'Outcome'
print("\nOutcome value counts:")
print(dataset['Outcome'].value_counts())

# Separate features (X) and target (Y)
X = dataset.drop(columns='Outcome', axis=1)
Y = dataset['Outcome']

# Standardize the feature data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nStandardized data (first 5 rows):")
print(X_scaled[:5])

# Update X to standardized data
X = X_scaled

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=2
)

# Check shapes of datasets
print("\n📦 Data shapes:")
print("Features (X):", X.shape)
print("Training set:", X_train.shape)
print("Test set:", X_test.shape)
