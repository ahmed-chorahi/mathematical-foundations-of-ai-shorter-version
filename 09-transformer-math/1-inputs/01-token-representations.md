# Token Representations

*📓 Notes · [09 · Transformer Mathematics](../README.md) · inputs*

**📝 In simple words:** Text is chopped into tokens, and each token is an integer ID.

**🔢 Small example:** `"I love AI"` → `["I", "love", "AI"]` → ids `[4, 17, 9]` (toy vocabulary).

**🤖 Why AI uses it:** models can only do math on numbers.

```python
import numpy as np
vocab = {"I": 4, "love": 17, "AI": 9}
ids = [vocab[t] for t in "I love AI".split()]; print(ids)
```

**🧪 Try it myself:** Ids for `"AI love I"`? <details><summary>Solution</summary>`[9, 17, 4]`.</details>

---
[Embeddings](../1-inputs/02-embeddings.md) →
