# Correlation

*📓 Notes · [04 · Statistics](../README.md) · describing data*

**📝 In simple words:** How strongly two variables move together, scaled to `[−1, 1]`.

**📐 Formula to remember:** `r = Cov(X,Y) / (σₓσᵧ)`

**🔢 Small example:** `X=[1,2,3]`, `Y=[2,4,7]` → `r ≈ 0.99` (almost a straight line).

**🤖 Why AI uses it:** feature selection (drop near-duplicate features), spotting leakage. **Correlation ≠ causation.**

```python
print(np.corrcoef([1, 2, 3], [2, 4, 7])[0, 1])
```

**🧪 Try it myself:** Correlation of `X=[1,2,3]`, `Y=[6,4,2]`? <details><summary>Solution</summary>`−1` (perfect negative line).</details>

---
← [Variance & Standard Deviation](../1-describing-data/02-variance-standard-deviation.md)  |  [Sampling](../2-sampling-and-confidence/04-sampling.md) →
