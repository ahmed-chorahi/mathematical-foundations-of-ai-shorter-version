# Linear Transformations

*📓 Notes · [01 · Linear Algebra](../README.md) · transformations and equations*

**📝 In simple words:** A matrix acting as a "move/stretch/rotate everything" machine.

**💡 Think of it like this:** Grid lines stay straight and the origin stays put.

**🔢 Small example:** rotate 90°: `R = [[0,−1],[1,0]]`, apply to `[1, 0]`.

**📐 Formula to remember:** `T(x) = Ax`

**✏️ Let me calculate it:** `[0·1 + (−1)·0, 1·1 + 0·0] = [0, 1]`. The x-axis arrow turned into the y-axis arrow.

**🤖 Why AI uses it:** each layer transforms the data into a new space where the task becomes easier.

```python
R = np.array([[0, -1], [1, 0]])
print(R @ np.array([1, 0]))   # [0 1]
```

**🧪 Try it myself:** What does `[[2,0],[0,1]]` do to `[1,1]`? <details><summary>Solution</summary>`[2,1]`, so it stretches x by 2.</details>

---
← [Distance](../2-operations-and-distance/07-distance.md)  |  [Systems of Equations](../3-transformations-and-equations/09-systems-of-equations.md) →
