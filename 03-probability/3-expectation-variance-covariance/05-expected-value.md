# Expected Value

*📓 Notes · [03 · Probability](../README.md) · expectation variance covariance*

**📝 In simple words:** The long-run average outcome.

**🔢 Small example:** fair die.

**📐 Formula to remember:** `𝔼[X] = Σ x · P(x)`

**✏️ Let me calculate it:** `(1+2+3+4+5+6)/6 = 3.5`.

**🤖 Why AI uses it:** the training loss is an *expected* loss over the data; cross-entropy is an expectation.

```python
x = np.arange(1, 7); p = np.full(6, 1/6)
print((x * p).sum())   # 3.5
```

**🧪 Try it myself:** Win $10 with prob 0.2, else lose $2. `𝔼`? <details><summary>Solution</summary>`10(0.2) − 2(0.8) = 0.4`.</details>

---
← [Bayes' Theorem](../2-conditional-and-bayes/04-bayes-theorem.md)  |  [Variance](../3-expectation-variance-covariance/06-variance.md) →
