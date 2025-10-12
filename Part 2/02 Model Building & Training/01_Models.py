# Imports
import pandas as pd
from sklearn.datasets import load_iris, make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, mean_squared_error
import tensorflow as tf
from tensorflow import keras
import numpy as np

# =====================================================
# 1. LINEAR REGRESSION (predict numbers)
# =====================================================
X_reg, y_reg = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
print("\n🔹 Linear Regression MSE:", mean_squared_error(y_test, y_pred))

# =====================================================
# 2. LOGISTIC REGRESSION (classification yes/no)
# =====================================================
iris = load_iris()
X = iris.data
y = (iris.target == 0).astype(int)   # Binary: Is it "Setosa" or not?
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
print("🔹 Logistic Regression Accuracy:", accuracy_score(y_test, y_pred))

# =====================================================
# 3. DECISION TREE
# =====================================================
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
y_pred = dtree.predict(X_test)
print("🔹 Decision Tree Accuracy:", accuracy_score(y_test, y_pred))

# =====================================================
# 4. RANDOM FOREST
# =====================================================
rforest = RandomForestClassifier(n_estimators=100, random_state=42)
rforest.fit(X_train, y_train)
y_pred = rforest.predict(X_test)
print("🔹 Random Forest Accuracy:", accuracy_score(y_test, y_pred))

# =====================================================
# 5. SUPPORT VECTOR MACHINE (SVM)
# =====================================================
svm = SVC(kernel="linear")
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
print("🔹 SVM Accuracy:", accuracy_score(y_test, y_pred))

# =====================================================
# 6. NEURAL NETWORK (Deep Learning with Keras)
# =====================================================
X = iris.data
y = iris.target  # 3 classes: Setosa, Versicolor, Virginica

# One-hot encode labels
y_onehot = keras.utils.to_categorical(y, 3)

X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)

model = keras.Sequential([
    keras.layers.Dense(10, activation="relu", input_shape=(4,)),
    keras.layers.Dense(10, activation="relu"),
    keras.layers.Dense(3, activation="softmax")   # 3 classes
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=50, verbose=0)

loss, acc = model.evaluate(X_test, y_test, verbose=0)
print("🔹 Neural Network Accuracy:", acc)
