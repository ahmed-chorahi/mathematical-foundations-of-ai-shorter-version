# Hessian

*📓 Notes · [02 · Calculus](../README.md) · many variables*

**📝 In simple words:** The matrix of *second* derivatives, describing the curvature.

**🔢 Small example:** `f(x,y) = x² + 3y²`

**📐 Formula to remember:** `H_ij = ∂²f/∂xᵢ∂xⱼ`

**✏️ Let me calculate it:** `H = [[2, 0],[0, 6]]`. Both positive → bowl shape → minimum.

**🤖 Why AI uses it:** it tells whether a flat spot is a min, max, or saddle; second-order optimizers use it, and it explains why some directions are harder to learn.

```python
H = np.array([[2, 0], [0, 6]])
print(np.linalg.eigvalsh(H))   # all > 0 → minimum
```

**🧪 Try it myself:** `f = x² − y²`. Min, max, or saddle? <details><summary>Solution</summary>`H = diag(2, −2)`, mixed signs → saddle.</details>

---
← [Jacobian](../2-many-variables/06-jacobian.md)  |  [Critical Points](../3-critical-points/08-critical-points.md) →
