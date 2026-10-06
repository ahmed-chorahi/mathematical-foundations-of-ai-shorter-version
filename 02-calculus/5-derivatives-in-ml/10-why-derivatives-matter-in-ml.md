# Why Derivatives Matter in ML

*📓 Notes · [02 · Calculus](../README.md) · derivatives in ml*

```text
 loss
  │\
  │ \
  │  \__          slope negative → move right
  │     \__/      slope zero     → stop (minimum)
  └──────────► weight
```

1. Define a **loss** (how wrong the model is).
2. Compute the **derivative** of loss with respect to each weight.
3. Move each weight a little **against** its derivative.
4. Repeat. That's learning.

```python
# learn w so that w*2 ≈ 6  (true w = 3)
w, lr = 0.0, 0.1
for _ in range(50):
    grad = 2 * (w*2 - 6) * 2     # d/dw of (2w − 6)²
    w -= lr * grad
print(round(w, 3))               # ≈ 3.0
```

**🧪 Try it myself:** In the code above, what's the loss derivative at `w=0`? <details><summary>Solution</summary>`2(−6)(2) = −24`: negative, so `w` increases.</details>

---
← [Integrals](../4-integrals/09-integrals.md)
