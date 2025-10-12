import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Training function
# -----------------------------
def train_linear_regression(X, Y, learning_rate, epochs):
    w, b = 0.0, 0.0  # parameters (start from zero)
    losses = []

    for epoch in range(epochs):
        # Predictions
        Y_pred = w * X + b

        # Loss (Mean Squared Error)
        loss = np.mean((Y - Y_pred) ** 2)
        losses.append(loss)

        # Gradients
        dw = -2 * np.mean(X * (Y - Y_pred))
        db = -2 * np.mean(Y - Y_pred)

        # Update parameters (using hyperparameters)
        w -= learning_rate * dw
        b -= learning_rate * db

    return w, b, losses

# -----------------------------
# Training Data
# -----------------------------
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)  # Perfect line y = 2x

# -----------------------------
# Try different learning rates
# -----------------------------
learning_rates = [0.001, 0.01, 0.1]
epochs = 100

plt.figure(figsize=(14, 5))

for lr in learning_rates:
    w, b, losses = train_linear_regression(X, Y, lr, epochs)
    plt.plot(losses, label=f"LR={lr}, Final w={w:.2f}, b={b:.2f}")

# Plot loss curves
plt.title("Effect of Learning Rate on Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()
