# The Neuron & Weighted Sum

*📓 Notes · [08 · Neural Network Mathematics](../README.md) · neuron layers forward*

**📝 In simple words:** Take inputs, weight them, add a bias.

**💡 Think of it like this:** Each weight says "how much do I care about this input?"

**🔢 Small example:** `x = [1, 2]`, `w = [0.5, −1]`, `b = 0.5`.

**📐 Formula to remember:** `z = w·x + b`

**✏️ Let me calculate it:** `0.5·1 + (−1)·2 + 0.5 = −1`.

```text
 x₁ ──w₁──╲
            ( Σ + b ) ──► activation ──► output
 x₂ ──w₂──╱
```

**🤖 Why AI uses it:** it's the dot product (01) plus a bias. A layer = many neurons = `Wx + b`.

```python
import numpy as np
x = np.array([1., 2.]); w = np.array([0.5, -1.]); b = 0.5
z = w @ x + b; print(z)   # -1.0
```

**🧪 Try it myself:** `w=[2,1]`, `x=[3,−4]`, `b=1`: z? <details><summary>Solution</summary>`6 − 4 + 1 = 3`.</details>

---
[Activation Functions](../1-neuron-layers-forward/02-activation-functions.md) →
