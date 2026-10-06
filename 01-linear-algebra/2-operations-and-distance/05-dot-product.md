# Dot Product

*📓 Notes · [01 · Linear Algebra](../README.md) · operations and distance*

**📝 In simple words:** Multiply matching entries and add.

**💡 Think of it like this:** Measures how much two vectors point the same way. Big positive = aligned, 0 = perpendicular, negative = opposite.

**🔢 Small example:** `a = [1,2,3]`, `b = [4,5,6]`

**📐 Formula to remember:** `a·b = Σ aᵢbᵢ = ‖a‖‖b‖ cos θ`

**✏️ Let me calculate it:** `1·4 + 2·5 + 3·6 = 4 + 10 + 18 = 32`

**🤖 Why AI uses it:** a neuron's weighted sum, attention scores, and cosine similarity are all dot products.

```python
a = np.array([1, 2, 3]); b = np.array([4, 5, 6])
print(a @ b)   # 32
```

**🧪 Try it myself:** `[2,−1]·[1,2]`? <details><summary>Solution</summary>`2 − 2 = 0`, so they are perpendicular.</details>

---
← [Matrix Operations](../2-operations-and-distance/04-matrix-operations.md)  |  [Norms](../2-operations-and-distance/06-norms.md) →
