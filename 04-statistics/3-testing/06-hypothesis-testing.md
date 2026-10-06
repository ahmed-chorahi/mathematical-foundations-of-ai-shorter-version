# Hypothesis Testing

*📓 Notes · [04 · Statistics](../README.md) · testing*

**📝 In simple words:** Asking "could this result be just luck?"

**✏️ Let me calculate it:** (1) null hypothesis H₀ ("nothing special") (2) compute a test statistic (3) see how surprising it is under H₀.

**🔢 Small example:** a coin lands heads 60 of 100 times. H₀: fair coin.

**📐 Formula to remember:** `z = (observed − expected) / SE`, with `SE = √(n p (1−p)) = 5`.

**✏️ Let me calculate it:** `z = (60 − 50)/5 = 2`.

**🤖 Why AI uses it:** comparing models, A/B tests, checking that an improvement isn't noise.

```python
z = (60 - 50) / np.sqrt(100 * 0.5 * 0.5); print(z)   # 2.0
```

**🧪 Try it myself:** 55 heads in 100 flips: z? <details><summary>Solution</summary>`5/5 = 1`, not surprising.</details>

---
← [Confidence Intervals](../2-sampling-and-confidence/05-confidence-intervals.md)  |  [p-values](../3-testing/07-p-values.md) →
