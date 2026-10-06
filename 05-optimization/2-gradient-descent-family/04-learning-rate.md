# Learning Rate

*📓 Notes · [05 · Optimization](../README.md) · gradient descent family*

**📝 In simple words:** The step size `α`.

**💡 Think of it like this:** Too small = slow. Too large = overshoot and diverge.

**✏️ Let me calculate it (α = 1.1):** `w₁ = 0 − 1.1(−6) = 6.6`, `grad = 7.2`, `w₂ = 6.6 − 7.92 = −1.32`. It bounces further away every step.

**🤖 Why AI uses it:** probably the most important hyperparameter in training.

```python
for lr in (0.01, 0.1, 1.1):
    w = 0.0
    for _ in range(20): w -= lr * 2 * (w - 3)
    print(lr, round(w, 3))     # slow, good, blows up
```

**🧪 Try it myself:** For this loss, what `α` jumps exactly to the minimum in one step? <details><summary>Solution</summary>`α = 0.5` (`w − 0.5·2(w−3) = 3`).</details>

---
← [Gradient Descent](../2-gradient-descent-family/03-gradient-descent.md)  |  [SGD & Mini-batch Gradient Descent](../2-gradient-descent-family/05-sgd-mini-batch-gradient-descent.md) →
