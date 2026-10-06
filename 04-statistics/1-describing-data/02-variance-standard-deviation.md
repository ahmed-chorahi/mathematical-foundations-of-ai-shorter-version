# Variance & Standard Deviation

*📓 Notes · [04 · Statistics](../README.md) · describing data*

**📝 In simple words:** The average squared distance from the mean, and its square root.

**📐 Formula to remember:** `s² = Σ(xᵢ − x̄)² / (n−1)`, `s = √s²` (sample version uses `n−1`).

**✏️ Let me calculate it:** deviations `[−3,−1,−1,1,4]` → squares `[9,1,1,1,16]` → sum 28 → `28/4 = 7` → `s ≈ 2.65`.

**🤖 Why AI uses it:** feature standardization `(x − μ)/σ`, LayerNorm, and weight-initialization scales.

```python
print(np.var(d, ddof=1), np.std(d, ddof=1))   # 7.0  2.645...
z = (np.array(d) - np.mean(d)) / np.std(d)
print(z.round(2))
```

**🧪 Try it myself:** Population variance of `[1,3]`? <details><summary>Solution</summary>mean 2, `(1+1)/2 = 1`.</details>

---
← [Mean, Median, Mode](../1-describing-data/01-mean-median-mode.md)  |  [Correlation](../1-describing-data/03-correlation.md) →
