# Projections

*📓 Notes · [01 · Linear Algebra](../README.md) · special directions*

**📝 In simple words:** The "shadow" of one vector on another.

**🔢 Small example:** project `a = [3,4]` onto `b = [1,0]`.

**📐 Formula to remember:** `proj_b(a) = (a·b / b·b) b`

**✏️ Let me calculate it:** `a·b = 3`, `b·b = 1` → `3·[1,0] = [3,0]`.

**🤖 Why AI uses it:** least-squares regression projects `y` onto the space of the features; PCA projects data onto top directions.

```python
a = np.array([3, 4]); b = np.array([1, 0])
print((a @ b) / (b @ b) * b)   # [3. 0.]
```

**🧪 Try it myself:** Project `[2,2]` onto `[0,1]`. <details><summary>Solution</summary>`(2/1)·[0,1] = [0, 2]`.</details>

---
← [Eigenvalues & Eigenvectors](../4-special-directions/10-eigenvalues-eigenvectors.md)  |  [Rank](../4-special-directions/12-rank.md) →
