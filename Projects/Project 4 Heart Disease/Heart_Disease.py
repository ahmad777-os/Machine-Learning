# importing dependencies
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pickle


# ----------------------------
# Data Preprocessing
# ----------------------------
dataframe = pd.read_csv('heart.csv')
print("First 5 rows:\n", dataframe.head())
print("DataFrame Shape:", dataframe.shape)

# ----------------------------
# Handling Missing Values
# ----------------------------
print("\nHandling Missing Values:")
print(dataframe.isnull().sum())

# ----------------------------
# Removing Duplicates
# ----------------------------
print("\nChecking Duplicates...")
print("Any duplicates? ", dataframe.duplicated().any())
print("Number of duplicates: ", dataframe.duplicated().sum())

# Drop duplicates (keep first occurrence)
dataframe = dataframe.drop_duplicates(keep="first")
print("Shape after removing duplicates:", dataframe.shape)

# ----------------------------
# Outlier Treatment (IQR Method)
# ----------------------------
num_cols = ["age", "trestbps", "chol", "thalach", "oldpeak"]

for col in num_cols:
    Q1 = dataframe[col].quantile(0.25)
    Q3 = dataframe[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Capping instead of removing
    dataframe[col] = np.where(dataframe[col] < lower_bound, lower_bound,
                              np.where(dataframe[col] > upper_bound, upper_bound, dataframe[col]))

print("\nOutlier treatment done (capped values).")

# ----------------------------
# Fixing DataTypes
# ----------------------------
print("\nDataTypes before conversion:\n", dataframe.dtypes)

categorical_cols = ["sex", "cp", "fbs", "restecg",
                    "exang", "slope", "ca", "thal", "target"]

for col in categorical_cols:
    dataframe[col] = dataframe[col].astype("category")

print("\nDataTypes after conversion:\n", dataframe.dtypes)

# ----------------------------
# Normalization / Standardization
# ----------------------------
scaler = StandardScaler()
dataframe[num_cols] = scaler.fit_transform(dataframe[num_cols])
print("\nStandardized numerical columns:\n", dataframe[num_cols].head())

# ----------------------------
# Encoding Categorical Variables
# ----------------------------
dataframe = pd.get_dummies(dataframe, columns=["cp", "restecg", "slope", "ca", "thal"], drop_first=True)
print("\nData after encoding:\n", dataframe.head())

# ----------------------------
# Feature Engineering
# ----------------------------
# Convert categorical back to numeric for arithmetic
dataframe["sex"] = dataframe["sex"].astype(int)
dataframe["fbs"] = dataframe["fbs"].astype(int)
dataframe["exang"] = dataframe["exang"].astype(int)
dataframe["target"] = dataframe["target"].astype(int)

dataframe["chol_per_age"] = dataframe["chol"] / (dataframe["age"] + 1e-6)
dataframe["hr_per_age"] = dataframe["thalach"] / (dataframe["age"] + 1e-6)
dataframe["risk_index"] = dataframe["oldpeak"] * dataframe["exang"]

print("\nData after Feature Engineering:\n", dataframe.head())
print("\nFinal Shape:", dataframe.shape)

# ----------------------------
# Splitting data for ML
# ----------------------------
X = dataframe.drop("target", axis=1)  # features
y = dataframe["target"]               # target

# ✅ Fix random_state for stable accuracy = 0.8512
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# ----------------------------
# Logistic Regression Model
# ----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", acc)
# Save the trained model
with open("heart_model.pkl", "wb") as f:
    pickle.dump(model, f)
