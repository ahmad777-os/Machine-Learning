# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Sample dataset: Weight (kg) vs Height (cm)
weight = np.array([40, 50, 60, 70, 80, 90, 100]).reshape(-1,1)
height = np.array([150, 160, 165, 172, 175, 178, 180])

# -----------------------------
# 1. Linear Regression (balanced model)
linear_model = LinearRegression()
linear_model.fit(weight, height)
height_pred_linear = linear_model.predict(weight)

# -----------------------------
# 2. Polynomial Regression (high variance if degree is high)
poly_model = make_pipeline(PolynomialFeatures(degree=5), LinearRegression())
poly_model.fit(weight, height)
height_pred_poly = poly_model.predict(weight)

# -----------------------------
# 3. High Bias Example: Mean predictor (ignores weight)
mean_height = np.mean(height) * np.ones_like(height)

# -----------------------------
# Plotting results
plt.figure(figsize=(10,6))
plt.scatter(weight, height, color='black', label='Actual Data', s=50)

# High Bias
plt.plot(weight, mean_height, color='red', linestyle='--', label='High Bias (Underfit)')

# Linear Regression
plt.plot(weight, height_pred_linear, color='blue', label='Balanced Model (Linear)')

# Polynomial Regression
plt.plot(weight, height_pred_poly, color='green', linestyle='-.', label='High Variance (Overfit)')

plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.title("Bias-Variance Tradeoff Example")
plt.legend()
plt.show()
