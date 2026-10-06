# Gradient Descent

*📓 Notes · [05 · Optimization](../README.md) · gradient descent family*

**📝 In simple words:** Repeatedly step downhill.

**📐 Formula to remember:** `w ← w − α ∇L(w)`

**🔢 Small example:** minimize `L(w) = (w − 3)²`, start `w = 0`, `α = 0.1`.

**✏️ Let me calculate it:**

```text
grad = 2(w − 3)
w₀=0      grad=−6      w₁ = 0 − 0.1(−6) = 0.6
w₁=0.6    grad=−4.8    w₂ = 0.6 + 0.48  = 1.08
w₂=1.08   grad=−3.84   w₃ = 1.464 ...→ 3
```

**🤖 Why AI uses it:** it's how every neural network is trained.

```python
w, lr = 0.0, 0.1
for step in range(30):
    w -= lr * 2 * (w - 3)
print(round(w, 4))   # ≈ 2.9988
```

**🧪 Try it myself:** One step from `w=5` on the same loss with `α=0.25`? <details><summary>Solution</summary>`grad=4`; `w = 5 − 1 = 4`.</details>

---
← [Local vs Global Minima](../1-what-to-minimize/02-local-vs-global-minima.md)  |  [Learning Rate](../2-gradient-descent-family/04-learning-rate.md) →
