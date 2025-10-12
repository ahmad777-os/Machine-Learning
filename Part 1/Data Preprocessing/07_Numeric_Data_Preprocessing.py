import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('diabetes.csv')

# Separate features and target
X = data.drop(columns='Outcome', axis=1)
Y = data['Outcome']

# Detect & remove outliers using IQR
Q1 = X.quantile(0.25)
Q3 = X.quantile(0.75)
IQR = Q3 - Q1

# Keep only rows without outliers
X_no_outliers = X[~((X < (Q1 - 1.5 * IQR)) | (X > (Q3 + 1.5 * IQR))).any(axis=1)]
Y_no_outliers = Y[X_no_outliers.index]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_no_outliers)

# Train/Test split
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y_no_outliers, test_size=0.2, random_state=2)

print("Before removing outliers:", X.shape)
print("After removing outliers:", X_no_outliers.shape)
