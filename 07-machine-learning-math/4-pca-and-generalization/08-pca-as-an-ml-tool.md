# PCA (as an ML tool)

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · pca and generalization*

**📝 In simple words:** Linear-algebra PCA from chapter 01, used to shrink features.

**✏️ Let me calculate it:** center → SVD → keep top-k directions → project. "Explained variance" `= σᵢ² / Σσ²`.

**🤖 Why AI uses it:** speed up training, visualize embeddings in 2D, denoise.

```python
rng = np.random.default_rng(1)
X = rng.normal(size=(100, 3)) @ np.array([[3, 0, 0], [0, 1, 0], [0, 0, 0.1]])
Xc = X - X.mean(0)
U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
print((S**2 / np.sum(S**2)).round(3))   # first component dominates
Z = Xc @ Vt[:2].T                       # 3D → 2D
```

**🧪 Try it myself:** If `S² = [90, 9, 1]`, how many components keep ≥ 95%? <details><summary>Solution</summary>Two (`99%`). One alone is 90%.</details>

---
← [Regularization](../3-likelihood-and-regularization/07-regularization.md)  |  [Bias–Variance Intuition](../4-pca-and-generalization/09-bias-variance-intuition.md) →
