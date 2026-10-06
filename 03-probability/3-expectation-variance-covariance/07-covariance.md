# Covariance

*📓 Notes · [03 · Probability](../README.md) · expectation variance covariance*

**📝 In simple words:** Whether two variables move together.

**📐 Formula to remember:** `Cov(X,Y) = 𝔼[(X−μₓ)(Y−μᵧ)]`

**🔢 Small example:** `X=[1,2,3]`, `Y=[2,4,6]`

**✏️ Let me calculate it:** means 2 and 4; products `(−1)(−2)+0+(1)(2) = 4`; divide by `n−1=2` → `2`. Positive → they rise together.

**🤖 Why AI uses it:** the covariance matrix is what PCA decomposes (01).

```python
X, Y = np.array([1, 2, 3]), np.array([2, 4, 6])
print(np.cov(X, Y))   # [[1,2],[2,4]]
```

**🧪 Try it myself:** Sign of `Cov` for `X=[1,2,3]`, `Y=[3,2,1]`? <details><summary>Solution</summary>Negative (they move oppositely).</details>

---
← [Variance](../3-expectation-variance-covariance/06-variance.md)  |  [Common Distributions](../4-distributions/08-common-distributions.md) →
