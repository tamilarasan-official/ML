from sklearn.mixture import GaussianMixture
import numpy as np

X = np.array([
    [1],
    [2],
    [3],
    [10],
    [11],
    [12]
])

gmm = GaussianMixture(
    n_components=2,
    random_state=0
)

gmm.fit(X)

print(gmm.predict(X))
