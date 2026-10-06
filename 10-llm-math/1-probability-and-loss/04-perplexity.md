# Perplexity

*📓 Notes · [10 · LLM Mathematics](../README.md) · probability and loss*

**📝 In simple words:** `e^(average loss)`: the effective number of choices the model hesitates between.

**📐 Formula to remember:** `PPL = exp(−(1/T) Σ log P(xₜ | x<ₜ))`

**✏️ Let me calculate it:** from step 1: average `= 4.605/3 = 1.535` → `PPL = e^1.535 = 4.64`. A model that is uniform over 100 tokens has `PPL = 100`.

**🤖 Why AI uses it:** the standard intrinsic metric; lower is better.

```python
nll = -np.mean(np.log(probs)); print(np.exp(nll))   # 4.64
print(np.exp(-np.log(1/100)))                        # 100
```

**🧪 Try it myself:** Average loss 2.0 nats: PPL? <details><summary>Solution</summary>`e² ≈ 7.39`.</details>

---
← [Cross-Entropy Objective & Log-Likelihood](../1-probability-and-loss/03-cross-entropy-objective-log-likelihood.md)  |  [Sampling & Temperature](../2-sampling/05-sampling-temperature.md) →
