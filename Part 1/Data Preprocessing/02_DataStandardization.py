# Importing Dependencies
import pandas as pd
import numpy as np
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Loading the dataset
dataset = sklearn.datasets.load_breast_cancer()

# Converting to Pandas DataFrame
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# Adding target column
df['target'] = dataset.target

print(df.head())
print("Shape:", df.shape)

# Separating features and target
X = df.drop(columns='target', axis=1)
Y = df['target']

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# Data Standardization
scaler = StandardScaler()

# Fit on training data, then transform both train & test
X_train_standardized = scaler.fit_transform(X_train)
X_test_standardized = scaler.transform(X_test)

# Check standard deviation after scaling
print("Std of original data:", np.std(dataset.data))
print("Std of standardized TRAIN data:", X_train_standardized.std())
print("Std of standardized TEST data:", X_test_standardized.std())
