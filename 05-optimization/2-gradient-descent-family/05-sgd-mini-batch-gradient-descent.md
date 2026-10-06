# SGD & Mini-batch Gradient Descent

*📓 Notes · [05 · Optimization](../README.md) · gradient descent family*

**📝 In simple words:** Use a small random chunk of data per step instead of everything.

**💡 Think of it like this:** Polling 32 people tells you roughly what 1 million think, and it's way cheaper.

**📐 Formula to remember:** `∇L ≈ (1/B) Σᵢ∈batch ∇ℓᵢ`

| Type | Batch size | Trait |
|---|---|---|
| Batch GD | all data | smooth, slow |
| SGD | 1 | noisy, fast |
| Mini-batch | 32–512 | the standard compromise |

**🤖 Why AI uses it:** datasets are too big to use in one step; noise even helps escape bad spots.

```python
import numpy as np
rng = np.random.default_rng(0)
X = rng.normal(size=1000); y = 3 * X + rng.normal(0, 0.1, 1000)
w, lr = 0.0, 0.1
for step in range(200):
    idx = rng.integers(0, 1000, 32)               # mini-batch of 32
    grad = np.mean(2 * (w * X[idx] - y[idx]) * X[idx])
    w -= lr * grad
print(round(w, 2))   # ≈ 3
```

**🧪 Try it myself:** 1,000 samples, batch 100: steps per epoch? <details><summary>Solution</summary>10.</details>

---
← [Learning Rate](../2-gradient-descent-family/04-learning-rate.md)  |  [Momentum](../3-smarter-optimizers/06-momentum.md) →
