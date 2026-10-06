# Summation Notation (Σ)

*📓 Notes · [00 · Prerequisites](../README.md) · exponents logs and sums*

**📝 In simple words:** Short way to write "add these up".

**💡 Think of it like this:** A `for` loop that keeps a running total.

**🔢 Small example:** `Σᵢ₌₁³ xᵢ` with `x = [2, 4, 6]`

**📐 Formula to remember:** `Σᵢ₌₁ⁿ xᵢ = x₁ + x₂ + … + xₙ`

**✏️ Let me calculate it:** `2 + 4 + 6 = 12`. The mean is `(1/n) Σ xᵢ = 12/3 = 4`.

**🤖 Why AI uses it:** Dot products, losses (average over data), and expectations are all sums.

```python
x = [2, 4, 6]
total = 0
for v in x: total += v
print(total, total/len(x))   # 12 4.0
```

**🧪 Try it myself:** Compute `Σ xᵢ²` for `x = [1, 2, 3]`.
<details><summary>Solution</summary>`1 + 4 + 9 = 14`.</details>

---
← [Exponents & Logarithms](../2-exponents-logs-and-sums/03-exponents-logarithms.md)  |  [Coordinate Systems & Basic Geometry](../3-geometry-and-coordinates/05-coordinate-systems-basic-geometry.md) →
