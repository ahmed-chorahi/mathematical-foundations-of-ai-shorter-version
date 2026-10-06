# Derivatives

*📓 Notes · [02 · Calculus](../README.md) · limits and derivatives*

**📝 In simple words:** The slope of a function at a point.

**💡 Think of it like this:** Speedometer reading: how fast the output changes right now.

**🔢 Small example:** `f(x) = x²` at `x = 3`.

**📐 Formula to remember:** `f′(x) = lim_{h→0} (f(x+h) − f(x)) / h`. Rules: `(xⁿ)′ = n xⁿ⁻¹`, `(eˣ)′ = eˣ`, `(ln x)′ = 1/x`.

**✏️ Let me calculate it:** `f′(x) = 2x` → `f′(3) = 6`. Check: `(3.001² − 3²)/0.001 ≈ 6.001`.

**🤖 Why AI uses it:** the slope of the loss tells us which way to move a weight.

```python
f = lambda x: x**2
h = 1e-5
print((f(3 + h) - f(3)) / h)   # ≈ 6
```

**🧪 Try it myself:** Derivative of `x³` at `x=2`? <details><summary>Solution</summary>`3x² = 12`.</details>

---
← [Functions & Limits](../1-limits-and-derivatives/01-functions-limits.md)  |  [Partial Derivatives](../2-many-variables/03-partial-derivatives.md) →
