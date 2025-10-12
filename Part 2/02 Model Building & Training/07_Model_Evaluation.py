from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ---------------- Regression Example ----------------
y_true_reg = [3, 5, 2.5, 7]
y_pred_reg = [2.5, 5, 4, 8]

print("Regression Evaluation:")
print("MAE:", mean_absolute_error(y_true_reg, y_pred_reg))
print("MSE:", mean_squared_error(y_true_reg, y_pred_reg))
print("R²:", r2_score(y_true_reg, y_pred_reg))

# ---------------- Classification Example ----------------
y_true_cls = [1, 0, 1, 1, 0, 1, 0]
y_pred_cls = [1, 0, 1, 0, 0, 1, 1]

print("\nClassification Evaluation:")
print("Accuracy:", accuracy_score(y_true_cls, y_pred_cls))
print("Precision:", precision_score(y_true_cls, y_pred_cls))
print("Recall:", recall_score(y_true_cls, y_pred_cls))
print("F1 Score:", f1_score(y_true_cls, y_pred_cls))
