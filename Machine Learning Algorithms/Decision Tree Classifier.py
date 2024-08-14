from sklearn.tree import DecisionTreeClassifier
import numpy as np

def decision_tree_classifier(X, y):
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf

# Example usage
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 1, 0, 1])
clf = decision_tree_classifier(X, y)
print(f"Decision Tree Classifier: {clf}")
