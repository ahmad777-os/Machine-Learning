import numpy as np
import pandas as pd

# Load dataset
data = pd.read_csv('credit_data.csv')
print("First five rows of Credit Dataset:\n", data.head())

# Check class distribution (Imbalanced dataset check)
print("\nClass distribution:\n", data['Class'].value_counts())

# Separate transactions into legitimate and fraudulent
legit = data[data['Class'] == 0]
fraud = data[data['Class'] == 1]

print("\nLegit shape:", legit.shape)
print("Fraud shape:", fraud.shape)

# Under-sampling: take a sample from legitimate transactions equal to fraud count
legit_sample = legit.sample(n=492)
print("\nLegit sample shape:", legit_sample.shape)

# Combine legit sample and all fraud transactions
new_data = pd.concat([legit_sample, fraud], axis=0)

# Show new dataset class distribution
print("\nNew class distribution:\n", new_data['Class'].value_counts())

# Display first rows of the balanced dataset
print("\nFirst five rows of new dataset:\n", new_data.head())
