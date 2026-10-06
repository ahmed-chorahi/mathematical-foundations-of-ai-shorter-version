# PCA Intuition

*📓 Notes · [01 · Linear Algebra](../README.md) · decompositions*

**📝 In simple words:** Rotate the data to find the directions with the most spread, keep the top ones.

**💡 Think of it like this:** A tilted cloud of points is mostly "long" in one direction. Describe each point by its position along that line.

```text
   •  • •
  • • • •        →   keep the long axis (PC1),
 • • • •             drop the thin one (PC2)
```

**✏️ Let me calculate it:** (1) center the data (2) covariance matrix (3) eigenvectors (4) project on top-k.

**🤖 Why AI uses it:** compress features, visualize high-dimensional data, remove noise.

```python
import numpy as np
rng = np.random.default_rng(0)
x = rng.normal(size=200); X = np.c_[x, 0.5*x + 0.1*rng.normal(size=200)]
Xc = X - X.mean(axis=0)
cov = Xc.T @ Xc / (len(Xc) - 1)
vals, vecs = np.linalg.eigh(cov)           # ascending order
print("variance per direction:", vals)      # one big, one tiny
pc1 = vecs[:, -1]; Z = Xc @ pc1             # 2D → 1D
print(Z.shape)
```

**🧪 Try it myself:** If eigenvalues are `[9, 1]`, how much variance does PC1 explain? <details><summary>Solution</summary>`9 / (9+1) = 90%`.</details>

---
← [Orthogonality](../4-special-directions/13-orthogonality.md)  |  [SVD Intuition](../5-decompositions/15-svd-intuition.md) →
