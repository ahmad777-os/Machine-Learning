from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LogisticRegression

# 1. Load dataset (Iris dataset)
data = load_iris()
X, y = data.data, data.target

# 2. Define model
model = LogisticRegression(max_iter=200)

# 3. Define K-Fold cross validation (5 folds)
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# 4. Run cross validation
scores = cross_val_score(model, X, y, cv=kfold)

print("Scores for each fold:", scores)
print("Average Accuracy:", scores.mean())



# If you want an even simpler way:
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.datasets import load_iris

# X, y = load_iris(return_X_y=True)
# model = LogisticRegression(max_iter=200)

# # 10-fold CV
# scores = cross_val_score(model, X, y, cv=10)
# print("Average Accuracy:", scores.mean())