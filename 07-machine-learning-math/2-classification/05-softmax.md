# Softmax

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · classification*

**📝 In simple words:** Turns any list of scores (logits) into probabilities.

**📐 Formula to remember:** `softmax(z)ᵢ = e^zᵢ / Σⱼ e^zⱼ`

**🔢 Small example:** `z = [2, 1, 0]`.

**✏️ Let me calculate it:** `e² = 7.389`, `e¹ = 2.718`, `e⁰ = 1` → sum `11.107` → `[0.665, 0.245, 0.090]`. All positive, sum to 1, bigger score → bigger share.

**Stability trick:** subtract `max(z)` first; the answer is unchanged but `e^1000` won't overflow.

**🤖 Why AI uses it:** multi-class output, attention weights (09), next-token probabilities (10).

```python
def softmax(z):
    e = np.exp(z - np.max(z))
    return e / e.sum()
print(softmax(np.array([2., 1., 0.])).round(3))   # [0.665 0.245 0.09]
```

**🧪 Try it myself:** `softmax([0, 0])`? <details><summary>Solution</summary>`[0.5, 0.5]`.</details>

---
← [Binary Cross-Entropy](../2-classification/04-binary-cross-entropy.md)  |  [Maximum Likelihood](../3-likelihood-and-regularization/06-maximum-likelihood.md) →
