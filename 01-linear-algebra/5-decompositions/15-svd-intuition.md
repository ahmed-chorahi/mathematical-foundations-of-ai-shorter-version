# SVD Intuition

*📓 Notes · [01 · Linear Algebra](../README.md) · decompositions*

**📝 In simple words:** Any matrix = rotate → stretch → rotate: `A = U Σ Vᵀ`.

**💡 Think of it like this:** It finds the most important "layers" of a matrix. Keep the largest singular values for a good approximation.

**📐 Formula to remember:** `A = Σᵢ σᵢ uᵢ vᵢᵀ` with `σ₁ ≥ σ₂ ≥ …`

**✏️ Let me calculate it:** keep only `σ₁` → rank-1 approximation of A.

**🤖 Why AI uses it:** image compression, recommender systems, LoRA (low-rank weight updates), and PCA is SVD in disguise.

```python
A = np.array([[3., 0.], [0., 1.]])
U, S, Vt = np.linalg.svd(A)
print(S)                                    # [3. 1.]
A1 = S[0] * np.outer(U[:, 0], Vt[0])        # rank-1 approximation
print(A1)
```

**🧪 Try it myself:** What's the rank-1 approximation error idea if `S = [10, 0.1]`? <details><summary>Solution</summary>Tiny, since the second layer barely contributes, so rank 1 keeps almost everything.</details>

---
← [PCA Intuition](../5-decompositions/14-pca-intuition.md)
