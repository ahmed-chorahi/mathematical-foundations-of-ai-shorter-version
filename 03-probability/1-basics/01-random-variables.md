# Random Variables

*📓 Notes · [03 · Probability](../README.md) · basics*

**📝 In simple words:** A variable whose value comes from a random process.

**💡 Think of it like this:** `X` = the number on a die before you roll.

**🔢 Small example:** `X ∈ {1,…,6}`, each with probability `1/6`.

**📐 Formula to remember:** `P(X = x)`; probabilities are `≥ 0` and sum to 1.

**✏️ Let me calculate it:** `P(X=4) = 1/6 ≈ 0.167`; `P(X even) = 3/6 = 0.5`.

**🤖 Why AI uses it:** a model's output ("cat" / "dog") or the next word is a random variable.

```python
import numpy as np
rng = np.random.default_rng(0)
rolls = rng.integers(1, 7, size=10000)
print((rolls % 2 == 0).mean())   # ≈ 0.5
```

**🧪 Try it myself:** Probability of rolling `> 4`? <details><summary>Solution</summary>`2/6 = 1/3`.</details>

---
[Probability Rules](../1-basics/02-probability-rules.md) →
