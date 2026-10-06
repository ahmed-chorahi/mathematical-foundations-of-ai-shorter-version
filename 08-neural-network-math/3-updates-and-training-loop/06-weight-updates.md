# Weight Updates

*📓 Notes · [08 · Neural Network Mathematics](../README.md) · updates and training loop*

**📐 Formula to remember:** `w ← w − α · ∂L/∂w`

**✏️ Let me calculate it (α = 0.1):** `w₂ = 0.5 − 0.1(−8) = 1.3`; `w₁ = 2 − 0.1(−2) = 2.2`. New forward: `h = 2.2`, `ŷ = 2.86`, `L = 0.0196` (down from 4).

```python
lr = 0.1
w2 -= lr * dw2; w1 -= lr * dw1
print(w1, w2, w2*max(0, w1*x))   # 2.2 1.3 2.86
```

**🧪 Try it myself:** If a gradient is positive, does the weight go up or down? <details><summary>Solution</summary>Down. We move against the gradient.</details>

---
← [Backpropagation & the Chain Rule](../2-loss-and-backprop/05-backpropagation-the-chain-rule.md)  |  [The Training Loop](../3-updates-and-training-loop/07-the-training-loop.md) →
