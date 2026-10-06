# Chain Rule

*📓 Notes · [02 · Calculus](../README.md) · many variables*

**📝 In simple words:** The derivative of a function inside a function.

**💡 Think of it like this:** Effects multiply along a chain: if A changes B by 2× and B changes C by 3×, A changes C by 6×.

**🔢 Small example:** `y = (3x + 1)²`

**📐 Formula to remember:** `dy/dx = dy/du · du/dx`

**✏️ Let me calculate it:** `u = 3x+1`: `dy/du = 2u`, `du/dx = 3` → `6(3x+1)`. At `x=1`: `24`.

**🤖 Why AI uses it:** a network is layers inside layers. Backpropagation *is* the chain rule applied layer by layer.

```python
f = lambda x: (3*x + 1)**2
h = 1e-5
print((f(1 + h) - f(1)) / h)   # ≈ 24
```

**🧪 Try it myself:** Derivative of `(2x)³` at `x=1`? <details><summary>Solution</summary>`3(2x)²·2 = 3·4·2 = 24`.</details>

---
← [Partial Derivatives](../2-many-variables/03-partial-derivatives.md)  |  [Gradients](../2-many-variables/05-gradients.md) →
