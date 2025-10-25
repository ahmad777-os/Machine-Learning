import numpy as np
class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
    
    # Sigmoid Function
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    # Fit the model to the data (Training)
    def fit(self, X, y):
        # number of samples (m), number of features (n)
        self.m, self.n = X.shape
        
        # initialize weights and bias
        self.w = np.zeros(self.n)
        self.b = 0
        
        # Gradient Descent
        for i in range(self.iterations):
            # Step 1: Linear combination
            z = np.dot(X, self.w) + self.b
            
            # Step 2: Sigmoid activation
            y_pred = self.sigmoid(z)
            
            # Step 3: Compute gradients
            dw = (1 / self.m) * np.dot(X.T, (y_pred - y))
            db = (1 / self.m) * np.sum(y_pred - y)
            
            # Step 4: Update weights and bias
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    # Predict probabilities
    def predict_proba(self, X):
        return self.sigmoid(np.dot(X, self.w) + self.b)
    
    # Predict classes (0 or 1)
    def predict(self, X):
        y_pred_proba = self.predict_proba(X)
        return np.where(y_pred_proba >= 0.5, 1, 0)
