# Coordinate Systems & Basic Geometry

*📓 Notes · [00 · Prerequisites](../README.md) · geometry and coordinates*

**📝 In simple words:** A way to describe position with numbers; and distance/angle between positions.

**💡 Think of it like this:** `(3, 4)` = 3 steps right, 4 steps up. Distance from origin is the hypotenuse.

**📐 Formula to remember:** `distance = √(x² + y²)` (Pythagoras). Angle from `cos θ = adjacent / hypotenuse`.

```text
 y
 4 |        • (3,4)
   |      /
   |    / 5
   |  /
   +-------- x
          3
```

**✏️ Let me calculate it:** `√(3² + 4²) = √25 = 5`

**🤖 Why AI uses it:** Data points are points in space. "Similar" means "close" or "same direction". 2D intuition carries to 1000D.

```python
import numpy as np
print(np.sqrt(3**2 + 4**2))   # 5.0
```

**🧪 Try it myself:** Distance from origin to `(5, 12)`?
<details><summary>Solution</summary>`√(25+144) = √169 = 13`.</details>

---
← [Summation Notation (Σ)](../2-exponents-logs-and-sums/04-summation-notation.md)  |  [Reading Notation](../4-notation/06-reading-notation.md) →
