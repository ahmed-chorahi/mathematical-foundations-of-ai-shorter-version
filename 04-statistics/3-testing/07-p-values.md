# p-values

*📓 Notes · [04 · Statistics](../README.md) · testing*

**📝 In simple words:** The probability of a result at least this extreme *if H₀ were true*.

**🔢 Small example:** `z = 2` → two-sided `p ≈ 0.046`.

**Rule of thumb:** `p < 0.05` is "statistically significant", but it's **not** the probability that H₀ is true, and it says nothing about effect size.

```python
from math import erf, sqrt
p = 2 * (1 - 0.5 * (1 + erf(2 / sqrt(2)))); print(round(p, 4))   # 0.0455
```

**🧪 Try it myself:** Is `z = 1` significant at 0.05? <details><summary>Solution</summary>`p ≈ 0.32`, so no.</details>

---
← [Hypothesis Testing](../3-testing/06-hypothesis-testing.md)  |  [Statistical Intuition for ML](../4-ml-intuition/08-statistical-intuition-for-ml.md) →
