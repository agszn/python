from sklearn.linear_model import LogisticRegression
import numpy as np

def logistic_regression(X, y):
    clf = LogisticRegression()
    clf.fit(X, y)
    return clf

# Example usage
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 1, 0, 1])
clf = logistic_regression(X, y)
print(f"Logistic Regression Model: {clf}")
