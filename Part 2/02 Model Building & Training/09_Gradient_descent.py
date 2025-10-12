import numpy as np
import matplotlib.pyplot as plt

# Training data (y = 2x)
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)

# Parameters (weights) - start randomly
w, b = 0.0, 0.0

# Hyperparameters
learning_rate = 0.01
epochs = 100

losses = []

# Training loop (Gradient Descent)
for epoch in range(epochs):
    Y_pred = w * X + b  # prediction

    # Loss (Mean Squared Error)
    loss = np.mean((Y - Y_pred) ** 2)
    losses.append(loss)

    # Gradients (derivatives)
    dw = -2 * np.mean(X * (Y - Y_pred))
    db = -2 * np.mean(Y - Y_pred)

    # Update parameters (step downhill)
    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 20 == 0:
        print(f"Epoch {epoch}: Loss={loss:.4f}, w={w:.4f}, b={b:.4f}")

# Final parameters
print("\nFinal learned parameters:")
print(f"w = {w:.4f}, b = {b:.4f}")

# Plot loss curve
plt.plot(range(epochs), losses, marker='o')
plt.title("Gradient Descent: Loss Curve")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.grid(True)
plt.show()
