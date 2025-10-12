import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Generate data (simple pattern + noise)
np.random.seed(0)
X = np.sort(np.random.rand(20, 1) * 5)  # temperatures
y = np.sin(X).ravel() + np.random.randn(20) * 0.2  # ice cream sales

# Underfit (linear), good fit (degree 3), overfit (degree 15)
degrees = [1, 3, 15]

plt.figure(figsize=(12, 4))
for i, d in enumerate(degrees, 1):
    model = make_pipeline(PolynomialFeatures(d), LinearRegression())
    model.fit(X, y)
    X_test = np.linspace(0, 5, 100).reshape(-1, 1)
    y_pred = model.predict(X_test)
    
    plt.subplot(1, 3, i)
    plt.scatter(X, y, color="black", label="Training Data")
    plt.plot(X_test, y_pred, label=f"Degree {d}")
    plt.legend()
    plt.title(f"Model Degree = {d}")

plt.show()
