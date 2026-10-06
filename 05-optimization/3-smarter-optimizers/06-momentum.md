# Momentum

*📓 Notes · [05 · Optimization](../README.md) · smarter optimizers*

**📝 In simple words:** Keep part of the previous direction, like a rolling ball.

**📐 Formula to remember:** `v ← βv + ∇L`, `w ← w − αv` (β ≈ 0.9)

**✏️ Let me calculate it:** gradients `−6` then `−4.8`: `v₁ = −6`; `v₂ = 0.9(−6) − 4.8 = −10.2`. The step grows when the direction stays consistent.

**🤖 Why AI uses it:** speeds up along valleys and smooths noisy mini-batch gradients.

```python
w, v = 0.0, 0.0
for _ in range(50):
    g = 2 * (w - 3); v = 0.9 * v + g; w -= 0.05 * v
print(round(w, 3))
```

**🧪 Try it myself:** If `v=2`, `β=0.9`, new gradient `1`: new `v`? <details><summary>Solution</summary>`1.8 + 1 = 2.8`.</details>

---
← [SGD & Mini-batch Gradient Descent](../2-gradient-descent-family/05-sgd-mini-batch-gradient-descent.md)  |  [Adam](../3-smarter-optimizers/07-adam.md) →
