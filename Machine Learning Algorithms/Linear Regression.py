import numpy as np

def linear_regression(X, y):
    X_b = np.c_[np.ones((X.shape[0], 1)), X]  # add bias term
    theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    return theta_best

# Example usage
X = np.array([[1], [2], [3]])
y = np.array([1, 2, 3])
theta = linear_regression(X, y)
print(f"Coefficients: {theta}")
