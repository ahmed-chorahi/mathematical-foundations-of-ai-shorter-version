# Gradients

*📓 Notes · [02 · Calculus](../README.md) · many variables*

**📝 In simple words:** The vector of all partial derivatives.

**💡 Think of it like this:** It points uphill, the direction of fastest increase. Go the opposite way to go downhill.

**🔢 Small example:** `f(x,y) = x² + y²` at `(1, 2)`.

**📐 Formula to remember:** `∇f = [∂f/∂x, ∂f/∂y]`

**✏️ Let me calculate it:** `∇f = [2x, 2y] = [2, 4]`. Downhill direction: `[−2, −4]`.

**🤖 Why AI uses it:** `∇Loss` tells every weight which way to move. Core of gradient descent.

```python
import numpy as np
grad = lambda p: 2 * p            # for f = x² + y²
print(grad(np.array([1., 2.])))   # [2. 4.]
```

**🧪 Try it myself:** Gradient of `x² + 3y` at `(2,5)`? <details><summary>Solution</summary>`[2x, 3] = [4, 3]`.</details>

---
← [Chain Rule](../2-many-variables/04-chain-rule.md)  |  [Jacobian](../2-many-variables/06-jacobian.md) →
