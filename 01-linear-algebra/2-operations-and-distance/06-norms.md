# Norms

*📓 Notes · [01 · Linear Algebra](../README.md) · operations and distance*

**📝 In simple words:** The length (size) of a vector.

**💡 Think of it like this:** How far the arrow reaches.

**🔢 Small example:** `x = [3, 4]`

**📐 Formula to remember:** `L2: ‖x‖ = √(Σxᵢ²)`, `L1: Σ|xᵢ|`

**✏️ Let me calculate it:** L2 = `√(9+16) = 5`; L1 = `3+4 = 7`.

**🤖 Why AI uses it:** regularization penalizes big weights (L1/L2); we normalize vectors to unit length.

```python
x = np.array([3, 4])
print(np.linalg.norm(x), np.linalg.norm(x, 1))   # 5.0 7.0
```

**🧪 Try it myself:** L2 norm of `[1, 2, 2]`? <details><summary>Solution</summary>`√(1+4+4) = 3`.</details>

---
← [Dot Product](../2-operations-and-distance/05-dot-product.md)  |  [Distance](../2-operations-and-distance/07-distance.md) →
