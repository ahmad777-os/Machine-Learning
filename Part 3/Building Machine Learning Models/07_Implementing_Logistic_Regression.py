import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        self.m, self.n = X.shape
        self.w = np.zeros(self.n)
        self.b = 0
        
        for i in range(self.iterations):
            z = np.dot(X, self.w) + self.b
            y_pred = self.sigmoid(z)
            dw = (1 / self.m) * np.dot(X.T, (y_pred - y))
            db = (1 / self.m) * np.sum(y_pred - y)
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict_proba(self, X):
        return self.sigmoid(np.dot(X, self.w) + self.b)
    
    def predict(self, X):
        y_pred_proba = self.predict_proba(X)
        return np.where(y_pred_proba >= 0.5, 1, 0)

dibetes_dataset = pd.read_csv('diabetes.csv')

X = dibetes_dataset.drop('Outcome', axis=1).values
y = dibetes_dataset['Outcome'].values

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(learning_rate=0.01, iterations=2000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)
