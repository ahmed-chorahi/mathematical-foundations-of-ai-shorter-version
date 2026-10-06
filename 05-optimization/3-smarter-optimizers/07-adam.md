# Adam

*📓 Notes · [05 · Optimization](../README.md) · smarter optimizers*

**📝 In simple words:** Momentum plus a per-weight adaptive step size.

**📐 Formula to remember:**

```text
m ← β₁m + (1−β₁)g           (average of gradients)
v ← β₂v + (1−β₂)g²          (average of squared gradients)
m̂ = m/(1−β₁ᵗ),  v̂ = v/(1−β₂ᵗ)
w ← w − α · m̂ / (√v̂ + ε)
```

**✏️ Let me calculate it (first step, g = −6):** `m = −0.6`, `v = 0.036`; `m̂ = −6`, `v̂ = 36`; step `= α·(−6)/6 = −α`. Each weight moves about `α` regardless of gradient scale.

**🤖 Why AI uses it:** the default optimizer for Transformers/LLMs (AdamW).

```python
w, m, v = 0.0, 0.0, 0.0
b1, b2, lr, eps = 0.9, 0.999, 0.1, 1e-8
for t in range(1, 201):
    g = 2 * (w - 3)
    m = b1*m + (1-b1)*g; v = b2*v + (1-b2)*g*g
    mh, vh = m/(1-b1**t), v/(1-b2**t)
    w -= lr * mh / (np.sqrt(vh) + eps)
print(round(w, 2))   # ≈ 3
```

**🧪 Try it myself:** Why divide by `√v̂`? <details><summary>Solution</summary>Weights with big gradients get smaller steps and weights with tiny gradients get larger ones.</details>

---
← [Momentum](../3-smarter-optimizers/06-momentum.md)  |  [Constrained Optimization](../4-constraints/08-constrained-optimization.md) →
