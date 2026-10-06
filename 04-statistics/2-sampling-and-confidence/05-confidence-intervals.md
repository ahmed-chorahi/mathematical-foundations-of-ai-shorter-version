# Confidence Intervals

*📓 Notes · [04 · Statistics](../README.md) · sampling and confidence*

**📝 In simple words:** A range likely to contain the true mean.

**📐 Formula to remember:** `x̄ ± 1.96 · s/√n` (about 95%).

**🔢 Small example:** `x̄ = 50`, `s = 10`, `n = 100`.

**✏️ Let me calculate it:** `SE = 1` → `50 ± 1.96` → `[48.04, 51.96]`.

**🤖 Why AI uses it:** "accuracy 91%" means little without error bars, especially on small test sets.

```python
m, s, n = 50, 10, 100
se = s / np.sqrt(n); print(m - 1.96*se, m + 1.96*se)
```

**🧪 Try it myself:** Same, but `n = 400`? <details><summary>Solution</summary>`SE=0.5` → `[49.02, 50.98]`.</details>

---
← [Sampling](../2-sampling-and-confidence/04-sampling.md)  |  [Hypothesis Testing](../3-testing/06-hypothesis-testing.md) →
