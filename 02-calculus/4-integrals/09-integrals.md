# Integrals

*📓 Notes · [02 · Calculus](../README.md) · integrals*

**📝 In simple words:** The area under a curve; the sum of tiny slices.

**🔢 Small example:** area under `f(x) = x` from 0 to 2.

**📐 Formula to remember:** `∫ₐᵇ f(x)dx ≈ Σ f(xᵢ)Δx`

**✏️ Let me calculate it:** `∫₀² x dx = x²/2 |₀² = 2`.

**🤖 Why AI uses it:** probabilities of continuous variables are areas; expected values are integrals.

```python
x = np.linspace(0, 2, 1001)
print(np.sum(x[:-1] * np.diff(x)))   # ≈ 2
```

**🧪 Try it myself:** `∫₀³ 2x dx`? <details><summary>Solution</summary>`x² |₀³ = 9`.</details>

---
← [Critical Points](../3-critical-points/08-critical-points.md)  |  [Why Derivatives Matter in ML](../5-derivatives-in-ml/10-why-derivatives-matter-in-ml.md) →
