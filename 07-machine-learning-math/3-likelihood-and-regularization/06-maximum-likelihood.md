# Maximum Likelihood

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · likelihood and regularization*

**📝 In simple words:** Choose parameters that make the observed data *most probable*.

**🔢 Small example:** a coin gave 7 heads out of 10. Which `p` fits best?

**📐 Formula to remember:** `L(p) = p⁷(1−p)³`; log-likelihood `ℓ = 7 ln p + 3 ln(1−p)`

**✏️ Let me calculate it:** `dℓ/dp = 7/p − 3/(1−p) = 0` → `p = 0.7`.

**The key link:** *minimizing cross-entropy = maximizing log-likelihood*. MSE is MLE under Gaussian noise; BCE is MLE under Bernoulli labels.

**🤖 Why AI uses it:** it's the principled reason behind our loss functions, including the LLM objective.

```python
ps = np.linspace(0.01, 0.99, 99)
ll = 7*np.log(ps) + 3*np.log(1-ps)
print(ps[np.argmax(ll)])   # 0.7
```

**🧪 Try it myself:** 3 heads in 4 flips: MLE of `p`? <details><summary>Solution</summary>`3/4 = 0.75`.</details>

---
← [Softmax](../2-classification/05-softmax.md)  |  [Regularization](../3-likelihood-and-regularization/07-regularization.md) →
