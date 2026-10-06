# Distance

*📓 Notes · [01 · Linear Algebra](../README.md) · operations and distance*

**📝 In simple words:** How far apart two points are: the norm of their difference.

**🔢 Small example:** `a = [1,1]`, `b = [4,5]`

**📐 Formula to remember:** `d(a,b) = ‖a − b‖`

**✏️ Let me calculate it:** `a−b = [−3,−4]` → `√(9+16) = 5`.

**Cosine similarity** (angle-based): `cos θ = a·b / (‖a‖‖b‖)`. For `[1,0]` and `[1,1]`: `1 / (1·1.414) = 0.707`.

**🤖 Why AI uses it:** k-NN, clustering, and embedding search ("find similar") all rely on distance or cosine similarity.

```python
a = np.array([1, 1]); b = np.array([4, 5])
print(np.linalg.norm(a - b))
u = np.array([1, 0]); w = np.array([1, 1])
print(u @ w / (np.linalg.norm(u) * np.linalg.norm(w)))   # 0.707
```

**🧪 Try it myself:** Distance between `[0,0]` and `[6,8]`? <details><summary>Solution</summary>10.</details>

---
← [Norms](../2-operations-and-distance/06-norms.md)  |  [Linear Transformations](../3-transformations-and-equations/08-linear-transformations.md) →
