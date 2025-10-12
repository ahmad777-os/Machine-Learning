import math
import matplotlib.pyplot as plt

# ------------------------------
# 1. Regression: Mean Squared Error (MSE)
# ------------------------------
def mean_squared_error(y_true, y_pred):
    errors = [(yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)]
    return sum(errors) / len(errors)

# Example
y_true_reg = [200, 250, 300]      # Actual values
y_pred_reg = [210, 240, 310]      # Predictions
mse_loss = mean_squared_error(y_true_reg, y_pred_reg)
print("MSE Loss (Regression):", mse_loss)


# ------------------------------
# 2. Classification: Cross-Entropy Loss
# ------------------------------
def cross_entropy_loss(y_true, y_pred):
    """
    y_true: actual class (one-hot encoded, e.g. [1, 0])
    y_pred: predicted probabilities (e.g. [0.9, 0.1])
    """
    loss = -sum([yt * math.log(yp + 1e-15) for yt, yp in zip(y_true, y_pred)])
    return loss

# Example
y_true_cls = [1, 0]       # Actual = Cat
y_pred_cls = [0.9, 0.1]   # Predicted probs
ce_loss = cross_entropy_loss(y_true_cls, y_pred_cls)
print("Cross-Entropy Loss (Classification):", ce_loss)


# ------------------------------
# 3. Training Simulation (Loss Decreasing)
# ------------------------------
losses = [100, 70, 40, 20, 10, 5, 2, 1]

for epoch, loss in enumerate(losses, 1):
    print(f"Epoch {epoch}: Loss = {loss}")

# Plot loss curve
plt.plot(range(1, len(losses)+1), losses, marker='o')
plt.title("Training Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()
