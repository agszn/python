from sklearn.cluster import KMeans
import numpy as np

def k_means(X, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    return kmeans.labels_, kmeans.cluster_centers_

# Example usage
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
labels, centers = k_means(X, 2)
print(f"Labels: {labels}")
print(f"Cluster Centers: {centers}")
