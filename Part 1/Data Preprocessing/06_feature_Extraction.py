import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
data = pd.read_csv('fake_news_dataset.csv')

# Fill missing values in the 'text' column
data['text'] = data['text'].fillna("")

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])

print("Shape of TF-IDF matrix:", X.shape)
