# Rank

*📓 Notes · [01 · Linear Algebra](../README.md) · special directions*

**📝 In simple words:** The number of truly independent rows/columns.

**💡 Think of it like this:** If one row is just a multiple of another, it adds no new information.

**🔢 Small example:** `[[1,2],[2,4]]`. Row 2 = 2 × row 1.

**📐 Formula to remember:** `rank(A) = dim(column space)`

**✏️ Let me calculate it:** only one independent row → rank 1 (not invertible).

**🤖 Why AI uses it:** redundant (correlated) features give low rank; low-rank structure is behind SVD, compression, and LoRA.

```python
print(np.linalg.matrix_rank(np.array([[1, 2], [2, 4]])))   # 1
```

**🧪 Try it myself:** Rank of `[[1,0],[0,1]]`? <details><summary>Solution</summary>2.</details>

---
← [Projections](../4-special-directions/11-projections.md)  |  [Orthogonality](../4-special-directions/13-orthogonality.md) →
