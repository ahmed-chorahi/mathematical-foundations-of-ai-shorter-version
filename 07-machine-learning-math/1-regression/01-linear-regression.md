# Linear Regression

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · regression*

**📝 In simple words:** Fit a line `ŷ = wx + b` to data.

**💡 Think of it like this:** Choose the line that sits closest to all points.

**🔢 Small example:** `x = [1,2,3]`, `y = [2,4,5]`.

**📐 Formula to remember:** `w = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²`, `b = ȳ − w x̄`

**✏️ Let me calculate it:** `x̄=2`, `ȳ=3.667`; numerator `3`, denominator `2` → `w = 1.5`, `b = 3.667 − 3 = 0.667`. Predictions: `[2.17, 3.67, 5.17]`.

**🤖 Why AI uses it:** the simplest model, and a neuron *is* linear regression plus an activation.

```python
import numpy as np
x = np.array([1., 2., 3.]); y = np.array([2., 4., 5.])
w = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean())**2)
b = y.mean() - w * x.mean()
print(w, b)                        # 1.5  0.667
# library equivalent: np.polyfit(x, y, 1)  or sklearn LinearRegression
print(np.polyfit(x, y, 1))
```

**🧪 Try it myself:** Predict at `x = 4`. <details><summary>Solution</summary>`1.5·4 + 0.667 = 6.667`.</details>

---
[MSE & MAE](../1-regression/02-mse-mae.md) →
