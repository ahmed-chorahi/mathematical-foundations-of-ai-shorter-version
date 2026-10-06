# Statistical Intuition for ML

*📓 Notes · [04 · Statistics](../README.md) · ml intuition*

| Statistics idea | ML version |
|---|---|
| sample vs population | train/test split |
| standard error shrinks with n | more data → steadier estimates |
| overfitting to noise | memorizing training samples |
| standardization | feature scaling, BatchNorm/LayerNorm |
| confidence interval | error bars on accuracy |
| outliers | MSE vs MAE choice |

```python
# a model's measured accuracy on a small test set is noisy
n, acc = 50, 0.9
print(1.96 * np.sqrt(acc*(1-acc)/n))   # ±~0.083, so 90% could really be 82–98%
```

**🧪 Try it myself:** Does going from 50 to 200 test samples help? <details><summary>Solution</summary>Yes, error halves (`√4 = 2`).</details>

---
← [p-values](../3-testing/07-p-values.md)
