import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load a Dataset
df = sns.load_dataset("tips")
print(df.head())
# styling 
sns.set_theme(style="whitegrid")  # Nice background
# 4. Key Plots for Machine Learning
# a) Distribution of a Feature (Understand feature spread)
sns.histplot(df["total_bill"], kde=True)
plt.show()
# b) Compare Categories
sns.boxplot(x="day", y="total_bill", data=df)
plt.show()
# c) Relationship Between Two Variables
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()
# d) Correlation Heatmap (Most used in ML!)
df_corr = df.corr(numeric_only=True)
sns.heatmap(df_corr, annot=True, cmap="coolwarm")
plt.show()
# e) Pairplot (Quick EDA)
sns.pairplot(df, hue="sex")
plt.show()
# 5. ML-Specific Usage Example
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df_iris = iris.frame

# Pairwise relationships with class color
sns.pairplot(df_iris, hue="target", palette="husl")
plt.show()

# Feature correlation
sns.heatmap(df_iris.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
