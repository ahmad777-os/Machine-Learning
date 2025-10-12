import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
cancer_data = pd.read_csv('breast_cancer_data.csv')

# Preview first 5 rows
print("\nFirst 5 rows of dataset:")
print(cancer_data.head())

# Check how many samples in each diagnosis category
print("\nDiagnosis value counts:")
print(cancer_data['diagnosis    '].value_counts())

# Initialize Label Encoder
label_encoder = LabelEncoder()

# Fit and transform the 'diagnosis' column
cancer_data['target'] = label_encoder.fit_transform(cancer_data['diagnosis'])

# Preview updated dataset
print("\nDataset with target column added:")
print(cancer_data.head())

# Check how many samples in each target class
print("\nTarget value counts:")
print(cancer_data['target'].value_counts())
