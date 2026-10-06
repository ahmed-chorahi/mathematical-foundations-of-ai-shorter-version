# Logistic Regression & the Sigmoid

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · classification*

**📝 In simple words:** Linear regression squashed into a probability for yes/no.

**📐 Formula to remember:** `p = σ(z) = 1/(1+e⁻ᶻ)`, with `z = w·x + b`

**🔢 Small example:** `w = 2`, `b = −1`, `x = 1`.

**✏️ Let me calculate it:** `z = 1` → `p = 1/(1+e⁻¹) = 0.731`. `z = 0` → 0.5; large `z` → near 1; very negative → near 0.

**🤖 Why AI uses it:** binary classification, and the sigmoid is a classic activation/gate.

```python
sigmoid = lambda z: 1 / (1 + np.exp(-z))
print(sigmoid(np.array([-4, 0, 1, 4])).round(3))   # [0.018 0.5 0.731 0.982]
```

**🧪 Try it myself:** `σ(0)`? <details><summary>Solution</summary>0.5.</details>

---
← [MSE & MAE](../1-regression/02-mse-mae.md)  |  [Binary Cross-Entropy](../2-classification/04-binary-cross-entropy.md) →
