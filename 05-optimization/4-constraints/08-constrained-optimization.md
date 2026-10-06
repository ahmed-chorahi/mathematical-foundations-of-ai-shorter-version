# Constrained Optimization

*📓 Notes · [05 · Optimization](../README.md) · constraints*

**📝 In simple words:** Minimize a loss while obeying a rule.

**🔢 Small example:** minimize `x² + y²` subject to `x + y = 1`.

**📐 Formula to remember (Lagrange):** `ℒ = f(x,y) + λ(x + y − 1)`; set all partial derivatives to 0.

**✏️ Let me calculate it:** `2x + λ = 0`, `2y + λ = 0` → `x = y`; `x + y = 1` → `x = y = 0.5`, value `0.5`.

**🤖 Why AI uses it:** L2/L1 regularization is a soft constraint on weight size; SVMs are constrained problems; softmax outputs must sum to 1.

```python
x = np.linspace(0, 1, 101); y = 1 - x
print(x[np.argmin(x**2 + y**2)])   # 0.5
```

**🧪 Try it myself:** Minimize `x² + y²` with `x + y = 4`. <details><summary>Solution</summary>`x = y = 2`, value 8.</details>

---
← [Adam](../3-smarter-optimizers/07-adam.md)
