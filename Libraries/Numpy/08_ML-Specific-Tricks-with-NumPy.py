# Feature Scaling (Normalization)
X = np.array([[1, 2], [3, 4], [5, 6]])
X_scaled = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
# One-Hot Encoding
labels = np.array([0, 1, 2])
one_hot = np.eye(3)[labels]
# Train-Test Split (without sklearn)
idx = np.random.permutation(len(X))
train_size = int(0.8 * len(X))
train_idx, test_idx = idx[:train_size], idx[train_size:]

X_train, X_test = X[train_idx], X[test_idx]
