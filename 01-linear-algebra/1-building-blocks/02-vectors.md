# Vectors

*📓 Notes · [01 · Linear Algebra](../README.md) · building blocks*

**📝 In simple words:** An ordered list of numbers.

**💡 Think of it like this:** An arrow from the origin, or a row in a spreadsheet. A house = `[size, rooms, age]`.

**🔢 Small example:** `x = [2, 3]`, `y = [1, 4]`

**📐 Formula to remember:** `x + y = [x₁+y₁, x₂+y₂]`

**✏️ Let me calculate it:** `[2,3] + [1,4] = [3, 7]`

```text
 y
 4|     • y
 3| • x
  |
  +--------- x
```

**🤖 Why AI uses it:** a data point, a word embedding, and the weights of a neuron are all vectors.

```python
x = np.array([2, 3]); y = np.array([1, 4])
print(x + y)   # [3 7]
```

**🧪 Try it myself:** `[1,2,3] + [4,0,−1]`? <details><summary>Solution</summary>`[5, 2, 2]`</details>

---
← [Scalars](../1-building-blocks/01-scalars.md)  |  [Matrices](../1-building-blocks/03-matrices.md) →
