import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = rng.normal(size=200)
X = np.c_[x, 0.5*x + 0.15*rng.normal(size=200)]
Xc = X - X.mean(axis=0)
vals, vecs = np.linalg.eigh(Xc.T @ Xc / (len(Xc)-1))
plt.scatter(Xc[:, 0], Xc[:, 1], s=8, alpha=.5)
for v, lam in zip(vecs.T, vals):
    plt.arrow(0, 0, *(v * np.sqrt(lam) * 2), color="red", width=0.02)
plt.axis("equal"); plt.title("PCA directions"); plt.savefig("pca.png", dpi=100)
print("eigenvalues:", vals)
