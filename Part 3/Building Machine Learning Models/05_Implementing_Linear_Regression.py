import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# -----------------------------
# Custom Linear Regression Class
# -----------------------------
class Linear_Regression:
    def __init__(self, learning_rate=0.01, no_of_iterations=1000):
        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations

    def fit(self, X, Y):
        self.m, self.n = X.shape
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        for i in range(self.no_of_iterations):
            self.update_weights()

    def update_weights(self):
        Y_pred = self.predict(self.X)
        dw = -(2 * (self.X.T).dot(self.Y - Y_pred)) / self.m
        db = -2 * np.sum(self.Y - Y_pred) / self.m
        self.w -= self.learning_rate * dw
        self.b -= self.learning_rate * db

    def predict(self, X):
        return X.dot(self.w) + self.b

# -----------------------------
# Data Handling
# -----------------------------
salary_data = pd.read_csv("salary_dataset.csv")

# Keep only the correct columns
X = salary_data[['YearsExperience']].values
Y = salary_data['Salary'].values

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=2)

# -----------------------------
# Model Training
# -----------------------------
model = Linear_Regression(learning_rate=0.02, no_of_iterations=1000)
model.fit(X_train, Y_train)

print("Weight:", model.w[0])
print("Bias:", model.b)

# -----------------------------
# Model Evaluation
# -----------------------------
Y_pred = model.predict(X_test)
print("Predicted Values:", Y_pred)

# -----------------------------
# Visualization
# -----------------------------
plt.scatter(X_test.flatten(), Y_test, color='red', label='Actual Data')
plt.plot(X_test.flatten(), Y_pred, color='blue', label='Predicted Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Experience vs Salary Prediction')
plt.legend()
plt.show()
