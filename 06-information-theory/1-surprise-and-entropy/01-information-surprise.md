# Information (Surprise)

*📓 Notes · [06 · Information Theory](../README.md) · surprise and entropy*

**📝 In simple words:** How surprising an event is. Rare events carry more information.

**💡 Think of it like this:** "The sun rose today" tells you nothing. "It snowed in the desert" tells you a lot.

**📐 Formula to remember:** `I(x) = −log₂ P(x)`

**✏️ Let me calculate it:** `P = 1/2` → 1 bit. `P = 1/8` → `−log₂(1/8) = 3` bits. `P = 1` → 0 bits.

**🤖 Why AI uses it:** the loss for one prediction is the surprise the model felt at the true answer: `−log P(correct)`.

```python
import numpy as np
for p in (1, 0.5, 0.125): print(p, -np.log2(p))
```

**🧪 Try it myself:** Information in an event with `P = 1/16`? <details><summary>Solution</summary>4 bits.</details>

---
[Entropy](../1-surprise-and-entropy/02-entropy.md) →
