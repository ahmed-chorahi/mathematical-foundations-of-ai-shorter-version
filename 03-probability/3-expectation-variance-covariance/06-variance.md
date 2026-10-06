# Variance

*📓 Notes · [03 · Probability](../README.md) · expectation variance covariance*

**📝 In simple words:** How spread out the outcomes are around the mean.

**📐 Formula to remember:** `Var(X) = 𝔼[(X − μ)²] = 𝔼[X²] − μ²`

**✏️ Let me calculate it (die):** `𝔼[X²] = (1+4+9+16+25+36)/6 = 15.17`; `Var = 15.17 − 3.5² = 2.92`.

**🤖 Why AI uses it:** noisy gradients, weight initialization scales, and the bias-variance tradeoff.

```python
print((x**2 * p).sum() - 3.5**2)   # ≈ 2.917
```

**🧪 Try it myself:** Variance of a coin (heads=1, tails=0)? <details><summary>Solution</summary>`μ=0.5`; `0.5(0.25)+0.5(0.25) = 0.25`.</details>

---
← [Expected Value](../3-expectation-variance-covariance/05-expected-value.md)  |  [Covariance](../3-expectation-variance-covariance/07-covariance.md) →
