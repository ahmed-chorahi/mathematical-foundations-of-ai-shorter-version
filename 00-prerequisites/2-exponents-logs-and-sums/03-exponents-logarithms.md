# Exponents & Logarithms

*📓 Notes · [00 · Prerequisites](../README.md) · exponents logs and sums*

**📝 In simple words:** `2³` means 2·2·2. A logarithm asks the reverse: "what power gives me this?"

**💡 Think of it like this:** Exponent = repeated multiplying. Log = counting how many multiplications. Logs turn products into sums.

**🔢 Small example:** `2³ = 8`, so `log₂(8) = 3`.

**📐 Formula to remember:**

```text
log(a·b) = log(a) + log(b)
log(a/b) = log(a) − log(b)
log(aⁿ)  = n·log(a)
e^(ln x) = x
```

**✏️ Let me calculate it:** `log(0.5 · 0.5 · 0.5) = 3·log(0.5) = 3 × (−0.693) = −2.079`

**🤖 Why AI uses it:** Probabilities get multiplied and become tiny. Logs make them sums and keep numbers stable. Softmax uses `e^x`; cross-entropy uses `log`.

```python
import numpy as np
print(np.log(0.5**3), 3*np.log(0.5))   # same
print(np.exp(np.log(5)))               # 5.0
```

**🧪 Try it myself:** Compute `log₂(32)`.
<details><summary>Solution</summary>`2⁵ = 32`, so the answer is 5.</details>

---
← [Functions](../1-algebra-and-functions/02-functions.md)  |  [Summation Notation (Σ)](../2-exponents-logs-and-sums/04-summation-notation.md) →
