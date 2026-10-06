# Objective & Loss Functions

*📓 Notes · [05 · Optimization](../README.md) · what to minimize*

**📝 In simple words:** A single number saying how bad the model currently is.

**💡 Think of it like this:** A score we want to push down.

**🔢 Small example:** predict `ŷ = 8` when truth is `y = 10`.

**📐 Formula to remember:** squared error `L = (y − ŷ)²`

**✏️ Let me calculate it:** `(10 − 8)² = 4`.

**🤖 Why AI uses it:** without a loss there's nothing to minimize. Details in chapter 07.

```python
y, y_hat = 10, 8
print((y - y_hat) ** 2)   # 4
```

**🧪 Try it myself:** Loss for `y=3`, `ŷ=5`? <details><summary>Solution</summary>`4`.</details>

---
[Local vs Global Minima](../1-what-to-minimize/02-local-vs-global-minima.md) →
