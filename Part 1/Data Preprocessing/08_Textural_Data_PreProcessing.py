# 08_Textual_Data_Preprocessing.py

"""
Textual Data Preprocessing Script
---------------------------------
This script demonstrates common preprocessing steps for text data before
feeding it into machine learning or NLP models.

Steps:
1. Lowercasing
2. Removing punctuation, numbers, and special characters
3. Removing stopwords
4. Tokenization
5. Lemmatization (or stemming)
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources (only the first time)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Example text data
texts = [
    "Hello there! This is a sample text for preprocessing.",
    "Text preprocessing is an essential step in NLP.",
    "Let's clean, tokenize, and lemmatize these sentences!"
]

def preprocess_text(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove numbers, punctuation, and special characters
    text = re.sub(r'[^a-z\s]', '', text)
    
    # 3. Tokenize
    tokens = nltk.word_tokenize(text)
    
    # 4. Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    # 5. Lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # 6. Join tokens back into string
    cleaned_text = ' '.join(tokens)
    
    return cleaned_text

# Apply preprocessing to all texts
cleaned_texts = [preprocess_text(t) for t in texts]

print("Original Texts:\n", texts)
print("\nCleaned Texts:\n", cleaned_texts)
