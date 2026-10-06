# Matrices

*📓 Notes · [01 · Linear Algebra](../README.md) · building blocks*

**📝 In simple words:** A grid of numbers (rows × columns).

**💡 Think of it like this:** A stack of vectors. A dataset: each row is one sample.

**🔢 Small example:** `A = [[1,2],[3,4]]` is 2×2.

**📐 Formula to remember:** `A ∈ ℝ^(m×n)` has m rows, n columns.

**✏️ Let me calculate it:** transpose flips rows and columns: `Aᵀ = [[1,3],[2,4]]`.

**🤖 Why AI uses it:** weights of a layer are a matrix; a batch of data is a matrix.

```python
A = np.array([[1, 2], [3, 4]])
print(A.shape, A.T)
```

**🧪 Try it myself:** Shape of a matrix with 100 images, each 784 pixels? <details><summary>Solution</summary>`(100, 784)`</details>

---
← [Vectors](../1-building-blocks/02-vectors.md)  |  [Matrix Operations](../2-operations-and-distance/04-matrix-operations.md) →
