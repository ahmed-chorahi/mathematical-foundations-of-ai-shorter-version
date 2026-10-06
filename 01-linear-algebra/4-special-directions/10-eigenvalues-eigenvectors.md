# Eigenvalues & Eigenvectors

*📓 Notes · [01 · Linear Algebra](../README.md) · special directions*

**📝 In simple words:** Special directions that a matrix only stretches, never turns.

**💡 Think of it like this:** Most vectors get knocked off course by a matrix. Eigenvectors stay on their line; the eigenvalue says how much they stretch.

**🔢 Small example:** `A = [[2,0],[0,3]]`

**📐 Formula to remember:** `Av = λv`

**✏️ Let me calculate it:** `A·[1,0] = [2,0] = 2·[1,0]` → λ = 2. `A·[0,1] = [0,3] = 3·[0,1]` → λ = 3.

**🤖 Why AI uses it:** PCA finds the eigenvectors of the covariance matrix: directions of biggest variance.

```python
A = np.array([[2, 0], [0, 3]])
vals, vecs = np.linalg.eig(A)
print(vals)   # [2. 3.]
```

**🧪 Try it myself:** Eigenvalues of `[[4,0],[0,1]]`? <details><summary>Solution</summary>4 and 1 (diagonal entries).</details>

---
← [Systems of Equations](../3-transformations-and-equations/09-systems-of-equations.md)  |  [Projections](../4-special-directions/11-projections.md) →
