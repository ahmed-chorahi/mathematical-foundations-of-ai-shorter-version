# Partial Derivatives

*📓 Notes · [02 · Calculus](../README.md) · many variables*

**📝 In simple words:** The derivative with respect to one variable, treating the others as constants.

**🔢 Small example:** `f(x, y) = x²y`

**📐 Formula to remember:** `∂f/∂x`, `∂f/∂y`

**✏️ Let me calculate it:** `∂f/∂x = 2xy`, `∂f/∂y = x²`. At `(2,3)`: `12` and `4`.

**🤖 Why AI uses it:** a model has millions of weights; each one gets its own partial derivative of the loss.

```python
f = lambda x, y: x**2 * y
h = 1e-5
print((f(2+h, 3) - f(2, 3)) / h, (f(2, 3+h) - f(2, 3)) / h)   # ≈ 12, 4
```

**🧪 Try it myself:** `∂/∂y` of `3xy + y²` at `(1,2)`? <details><summary>Solution</summary>`3x + 2y = 3 + 4 = 7`.</details>

---
← [Derivatives](../1-limits-and-derivatives/02-derivatives.md)  |  [Chain Rule](../2-many-variables/04-chain-rule.md) →
