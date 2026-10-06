# Critical Points

*📓 Notes · [02 · Calculus](../README.md) · critical points*

**📝 In simple words:** Places where the gradient is zero.

**🔢 Small example:** `f(x) = x² − 4x + 5`

**📐 Formula to remember:** `f′(x) = 0`; `f″ > 0` → min, `f″ < 0` → max.

**✏️ Let me calculate it:** `f′ = 2x − 4 = 0` → `x = 2`; `f″ = 2 > 0` → minimum, `f(2) = 1`.

**🤖 Why AI uses it:** training aims for a point where the gradient is ~0 (a minimum of loss).

```python
f = lambda x: x**2 - 4*x + 5
xs = np.linspace(-1, 5, 7); print(xs[np.argmin(f(xs))])   # 2.0
```

**🧪 Try it myself:** Critical point of `x² + 6x`? <details><summary>Solution</summary>`2x + 6 = 0` → `x = −3`.</details>

---
← [Hessian](../2-many-variables/07-hessian.md)  |  [Integrals](../4-integrals/09-integrals.md) →
