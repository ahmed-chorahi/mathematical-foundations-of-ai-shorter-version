# Sampling

*📓 Notes · [04 · Statistics](../README.md) · sampling and confidence*

**📝 In simple words:** Studying a small group to learn about a big one.

**💡 Think of it like this:** Averages of bigger samples wobble less. The standard error is `σ/√n`: 4× the data = half the noise.

**🤖 Why AI uses it:** a training set is a sample of the real world; a test set estimates future performance; mini-batches are samples (05).

```python
rng = np.random.default_rng(0)
pop = rng.normal(50, 10, 100_000)
for n in (10, 100, 1000):
    means = [rng.choice(pop, n).mean() for _ in range(500)]
    print(n, np.std(means).round(2))   # ≈ 10/√n
```

**🧪 Try it myself:** SE for σ=10, n=25? <details><summary>Solution</summary>`10/5 = 2`.</details>

---
← [Correlation](../1-describing-data/03-correlation.md)  |  [Confidence Intervals](../2-sampling-and-confidence/05-confidence-intervals.md) →
