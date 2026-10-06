# Common Distributions

*📓 Notes · [03 · Probability](../README.md) · distributions*

| Name | Models | Formula | Example |
|---|---|---|---|
| Bernoulli(p) | one yes/no | `P(1)=p` | one coin |
| Binomial(n,p) | # of yeses in n tries | `C(n,k)pᵏ(1−p)ⁿ⁻ᵏ` | heads in 10 flips |
| Categorical | one of K classes | `P(k)=pₖ` | next word |
| Uniform | all equal | `1/(b−a)` | random init |
| Normal(μ,σ²) | bell curve | `1/(σ√2π) e^(−(x−μ)²/2σ²)` | noise, weights |

**✏️ Let me calculate it (binomial):** `P(2 heads in 3 flips) = 3 · 0.5² · 0.5 = 0.375`.

**🤖 Why AI uses it:** Bernoulli → binary classification; Categorical → softmax output; Normal → noise, weight init, Gaussian assumptions.

```python
from math import comb
print(comb(3, 2) * 0.5**3)                # 0.375
w = np.random.default_rng(0).normal(0, 0.1, size=5)   # weight init
print(w)
```

**🧪 Try it myself:** P(exactly 1 head in 2 flips)? <details><summary>Solution</summary>`2 · 0.5 · 0.5 = 0.5`.</details>

---
← [Covariance](../3-expectation-variance-covariance/07-covariance.md)  |  [Joint Distributions](../4-distributions/09-joint-distributions.md) →
