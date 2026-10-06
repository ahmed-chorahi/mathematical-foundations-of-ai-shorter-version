# Matrix Operations

*📓 Notes · [01 · Linear Algebra](../README.md) · operations and distance*

**📝 In simple words:** Add, scale, and multiply matrices.

**💡 Think of it like this:** Matrix × vector = each row takes a weighted sum of the vector. (It's many dot products at once.)

**🔢 Small example:** `A = [[1,2],[3,4]]`, `v = [5,6]`

**📐 Formula to remember:** `(Av)ᵢ = Σⱼ Aᵢⱼ vⱼ`. For `A(m×n) · B(n×p)` the result is `m×p`.

**✏️ Let me calculate it:** row 1: `1·5 + 2·6 = 17`; row 2: `3·5 + 4·6 = 39` → `[17, 39]`

**🤖 Why AI uses it:** `y = Wx + b` is a neural-network layer.

```python
A = np.array([[1, 2], [3, 4]]); v = np.array([5, 6])
print(A @ v)   # [17 39]
B = np.array([[0, 1], [1, 0]])
print(A @ B)   # swaps columns of A
```

**🧪 Try it myself:** `[[2,0],[0,3]] · [4,5]`? <details><summary>Solution</summary>`[8, 15]`. It just scales each coordinate.</details>

---
← [Matrices](../1-building-blocks/03-matrices.md)  |  [Dot Product](../2-operations-and-distance/05-dot-product.md) →
