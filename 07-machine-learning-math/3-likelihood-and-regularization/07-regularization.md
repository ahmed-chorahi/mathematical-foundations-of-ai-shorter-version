# Regularization

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · likelihood and regularization*

**📝 In simple words:** Add a penalty for large weights to stop overfitting.

**📐 Formula to remember:** `L_total = L_data + λ‖w‖²` (L2/ridge) or `λ Σ|wᵢ|` (L1/lasso)

**🔢 Small example:** `w = [3, 4]`, `λ = 0.1`.

**✏️ Let me calculate it:** L2 penalty `= 0.1·(9+16) = 2.5`. The gradient adds `2λw`, so every update also shrinks `w` a bit ("weight decay"). L1 tends to push weights to exactly 0 (sparse).

**🤖 Why AI uses it:** weight decay is standard in training Transformers (AdamW).

```python
w = np.array([3., 4.]); lam = 0.1
print(lam * np.sum(w**2), lam * np.sum(np.abs(w)))   # 2.5  0.7
```

**🧪 Try it myself:** L2 penalty for `w=[1,1,1]`, `λ=0.5`? <details><summary>Solution</summary>`0.5·3 = 1.5`.</details>

---
← [Maximum Likelihood](../3-likelihood-and-regularization/06-maximum-likelihood.md)  |  [PCA (as an ML tool)](../4-pca-and-generalization/08-pca-as-an-ml-tool.md) →
