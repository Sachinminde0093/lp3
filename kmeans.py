import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("sales_data_sample.csv", encoding='latin')

X = df.iloc[:, [3, 4]].values

ss = StandardScaler()
scaled = ss.fit_transform(X)

wcss = []
for i in range(1, 11):
    clustering = KMeans(n_clusters=i, init="k-means++", random_state=42, n_init=10)
    clustering.fit(scaled)
    wcss.append(clustering.inertia_)

ks = range(1, 11)
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow method")
plt.xlabel("K value")
plt.ylabel("WCSS")
plt.show()

optimal_clusters = 3

kmeans = KMeans(n_clusters=optimal_clusters, init="k-means++", random_state=42, n_init=10)
kmeans.fit(scaled)

df['Cluster'] = kmeans.labels_

plt.scatter(scaled[:, 0], scaled[:, 1], c=kmeans.labels_, cmap='viridis', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroids')
plt.title(f'K-Means Clustering with {optimal_clusters} Clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()