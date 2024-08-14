from sklearn.svm import SVC
import numpy as np

def svm_classifier(X, y):
    clf = SVC()
    clf.fit(X, y)
    return clf

# Example usage
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 1, 0, 1])
clf = svm_classifier(X, y)
print(f"SVM Classifier: {clf}")
