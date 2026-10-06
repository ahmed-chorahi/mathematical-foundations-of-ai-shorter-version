# Systems of Equations

*📓 Notes · [01 · Linear Algebra](../README.md) · transformations and equations*

**📝 In simple words:** Several equations solved together: `Ax = b`.

**🔢 Small example:** `x + y = 3`, `x − y = 1`

**📐 Formula to remember:** `x = A⁻¹ b` (when A is invertible)

**✏️ Let me calculate it:** add them: `2x = 4`, so `x = 2`, `y = 1`.

**🤖 Why AI uses it:** linear regression has a closed-form solution that solves exactly such a system (the "normal equation").

```python
A = np.array([[1, 1], [1, -1]]); b = np.array([3, 1])
print(np.linalg.solve(A, b))   # [2. 1.]
```

**🧪 Try it myself:** Solve `2x + y = 5`, `x − y = 1`. <details><summary>Solution</summary>Add: `3x = 6`, `x = 2`, `y = 1`.</details>

---
← [Linear Transformations](../3-transformations-and-equations/08-linear-transformations.md)  |  [Eigenvalues & Eigenvectors](../4-special-directions/10-eigenvalues-eigenvectors.md) →
