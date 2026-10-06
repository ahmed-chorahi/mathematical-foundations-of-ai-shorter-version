# Cross-Entropy Objective & Log-Likelihood

*📓 Notes · [10 · LLM Mathematics](../README.md) · probability and loss*

**📝 In simple words:** Training pushes up the probability of the *actual* next token.

**📐 Formula to remember:** `L = −(1/T) Σₜ log P(xₜ | x<ₜ)`: the negative average log-likelihood (06, 07).

**✏️ Let me calculate it:** truth is "dog" → `−ln 0.245 = 1.406`. After training makes it `0.8` → `0.223`.

**🤖 Why AI uses it:** this single loss, averaged over trillions of tokens, is how GPT-style models are trained. Gradient w.r.t. logits is `p − onehot` (08).

```python
print(-np.log(p[1]), -np.log(0.8))
```

**🧪 Try it myself:** Loss if the model gave the true token probability 1? <details><summary>Solution</summary>`−ln 1 = 0`.</details>

---
← [Next-Token Prediction](../1-probability-and-loss/02-next-token-prediction.md)  |  [Perplexity](../1-probability-and-loss/04-perplexity.md) →
