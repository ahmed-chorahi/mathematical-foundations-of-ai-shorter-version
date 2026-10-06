# Next-Token Prediction

*📓 Notes · [10 · LLM Mathematics](../README.md) · probability and loss*

**📝 In simple words:** The model outputs one score (logit) per vocab token; softmax makes probabilities.

**🔢 Small example:** vocab `[cat, dog, car]`, logits `[2, 1, 0]`.

**✏️ Let me calculate it:** softmax → `[0.665, 0.245, 0.090]`. The model thinks "cat" is most likely.

```python
def softmax(z):
    e = np.exp(z - np.max(z)); return e / e.sum()
p = softmax(np.array([2., 1., 0.])); print(p.round(3))
```

**🧪 Try it myself:** Logits `[0,0,0]`: probabilities? <details><summary>Solution</summary>`[⅓, ⅓, ⅓]`.</details>

---
← [Language-Model Probability](../1-probability-and-loss/01-language-model-probability.md)  |  [Cross-Entropy Objective & Log-Likelihood](../1-probability-and-loss/03-cross-entropy-objective-log-likelihood.md) →
