# Language-Model Probability

*📓 Notes · [10 · LLM Mathematics](../README.md) · probability and loss*

**📝 In simple words:** The probability of a sentence, built with the chain rule of probability (03).

**📐 Formula to remember:** `P(x₁…x_T) = Π P(xₜ | x₁…xₜ₋₁)`

**🔢 Small example:** `"I love AI"`: `P(I)=0.1`, `P(love | I)=0.2`, `P(AI | I love)=0.5`.

**✏️ Let me calculate it:** `0.1 × 0.2 × 0.5 = 0.01`. Take logs so it's a sum: `ln 0.1 + ln 0.2 + ln 0.5 = −4.605`.

**🤖 Why AI uses it:** this factorization is *why* next-token prediction is enough to model all text.

```python
import numpy as np
probs = [0.1, 0.2, 0.5]
print(np.prod(probs), np.sum(np.log(probs)))   # 0.01  -4.605
```

**🧪 Try it myself:** Probabilities `[0.5, 0.5, 0.5, 0.5]`: sentence probability? <details><summary>Solution</summary>`1/16 = 0.0625`.</details>

---
[Next-Token Prediction](../1-probability-and-loss/02-next-token-prediction.md) →
