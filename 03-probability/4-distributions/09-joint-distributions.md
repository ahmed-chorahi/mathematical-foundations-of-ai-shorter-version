# Joint Distributions

*📓 Notes · [03 · Probability](../README.md) · distributions*

**📝 In simple words:** Probabilities of two variables together.

**🔢 Small example:** weather × umbrella:

| | umbrella | no umbrella | **marginal** |
|---|---|---|---|
| rain | 0.30 | 0.05 | **0.35** |
| sun | 0.10 | 0.55 | **0.65** |

**📐 Formula to remember:** marginal `P(X) = Σᵧ P(X,Y)`; conditional `P(Y|X) = P(X,Y)/P(X)`.

**✏️ Let me calculate it:** `P(umbrella | rain) = 0.30 / 0.35 ≈ 0.857`.

**🤖 Why AI uses it:** the probability of a whole sentence is a joint distribution over tokens, factored into conditionals (chain rule of probability) in chapter 10.

```python
J = np.array([[0.30, 0.05], [0.10, 0.55]])
print(J.sum(axis=1), J[0, 0] / J[0].sum())
```

**🧪 Try it myself:** `P(rain | umbrella)`? <details><summary>Solution</summary>`0.30 / (0.30+0.10) = 0.75`.</details>

---
← [Common Distributions](../4-distributions/08-common-distributions.md)
