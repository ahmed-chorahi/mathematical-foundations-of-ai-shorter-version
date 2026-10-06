# Functions & Limits

*📓 Notes · [02 · Calculus](../README.md) · limits and derivatives*

**📝 In simple words:** A limit is the value a function approaches as `x` gets close to a point.

**💡 Think of it like this:** Zoom in until you can't tell the difference.

**🔢 Small example:** `f(x) = (x² − 1)/(x − 1)` at `x → 1`. Can't plug in 1 (0/0), but it simplifies.

**📐 Formula to remember:** `lim_{x→a} f(x)`

**✏️ Let me calculate it:** `(x−1)(x+1)/(x−1) = x+1` → limit is `2`.

**🤖 Why AI uses it:** a derivative *is* a limit; it's the foundation under everything below.

```python
f = lambda x: (x**2 - 1) / (x - 1)
for x in [1.1, 1.01, 1.001]: print(x, f(x))   # → 2
```

**🧪 Try it myself:** `lim_{x→2} (x²−4)/(x−2)`? <details><summary>Solution</summary>`x+2 → 4`.</details>

---
[Derivatives](../1-limits-and-derivatives/02-derivatives.md) →
