# Orthogonality

*📓 Notes · [01 · Linear Algebra](../README.md) · special directions*

**📝 In simple words:** Perpendicular: dot product = 0.

**🔢 Small example:** `[1,1]` and `[1,−1]`: `1 − 1 = 0`.

**📐 Formula to remember:** `a ⊥ b ⇔ a·b = 0`

**🤖 Why AI uses it:** orthogonal directions carry independent information (PCA components are orthogonal); orthogonal initialization helps training stability.

```python
print(np.array([1, 1]) @ np.array([1, -1]))   # 0
```

**🧪 Try it myself:** Is `[2,3]` ⊥ `[3,−2]`? <details><summary>Solution</summary>`6 − 6 = 0`. Yes.</details>

---
← [Rank](../4-special-directions/12-rank.md)  |  [PCA Intuition](../5-decompositions/14-pca-intuition.md) →
