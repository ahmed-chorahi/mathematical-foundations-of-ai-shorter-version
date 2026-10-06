# Jacobian

*📓 Notes · [02 · Calculus](../README.md) · many variables*

**📝 In simple words:** The matrix of derivatives for a function with many inputs *and* many outputs.

**🔢 Small example:** `f(x,y) = [x+y, xy]`

**📐 Formula to remember:** `J_ij = ∂fᵢ/∂xⱼ`

**✏️ Let me calculate it:** `J = [[1, 1],[y, x]]`. At `(2,3)`: `[[1,1],[3,2]]`.

**🤖 Why AI uses it:** a layer maps a vector to a vector; backprop multiplies Jacobians (e.g., the softmax Jacobian).

```python
J = lambda x, y: np.array([[1, 1], [y, x]])
print(J(2, 3))
```

**🧪 Try it myself:** Jacobian of `[2x, x+3y]`? <details><summary>Solution</summary>`[[2,0],[1,3]]`.</details>

---
← [Gradients](../2-many-variables/05-gradients.md)  |  [Hessian](../2-many-variables/07-hessian.md) →
