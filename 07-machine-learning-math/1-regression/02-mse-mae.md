# MSE & MAE

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · regression*

**📝 In simple words:** Two ways to average the errors.

**📐 Formula to remember:** `MSE = (1/n) Σ(y − ŷ)²`, `MAE = (1/n) Σ|y − ŷ|`

**🔢 Small example:** `y = [3,5,7]`, `ŷ = [2,5,10]` → errors `[−1, 0, 3]`.

**✏️ Let me calculate it:** MSE `= (1+0+9)/3 = 3.33`; MAE `= (1+0+3)/3 = 1.33`. MSE punishes the big miss (3) much more.

**🤖 Why AI uses it:** MSE is smooth and standard for regression; MAE is robust to outliers.

```python
y = np.array([3, 5, 7]); yh = np.array([2, 5, 10])
print(np.mean((y - yh)**2), np.mean(np.abs(y - yh)))
```

**🧪 Try it myself:** MSE for `y=[1,2]`, `ŷ=[2,4]`? <details><summary>Solution</summary>`(1+4)/2 = 2.5`.</details>

---
← [Linear Regression](../1-regression/01-linear-regression.md)  |  [Logistic Regression & the Sigmoid](../2-classification/03-logistic-regression-the-sigmoid.md) →
