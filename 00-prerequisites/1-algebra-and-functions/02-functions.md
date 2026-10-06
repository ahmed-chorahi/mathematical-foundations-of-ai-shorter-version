# Functions

*📓 Notes · [00 · Prerequisites](../README.md) · algebra and functions*

**📝 In simple words:** A machine: number in, number out. `f(x)`.

**💡 Think of it like this:** A neuron is a function. A whole network is functions chained together.

**🔢 Small example:** `f(x) = 2x + 1`

**📐 Formula to remember:** `y = f(x)`; composition: `g(f(x))` means "do f, then g".

**✏️ Let me calculate it:** `f(3) = 2·3 + 1 = 7`. If `g(x) = x²`, then `g(f(3)) = 7² = 49`.

**🤖 Why AI uses it:** Layers are composed functions. The chain rule (chapter 02) exists because of composition.

```python
f = lambda x: 2*x + 1
g = lambda x: x**2
print(g(f(3)))   # 49
```

**🧪 Try it myself:** With `f(x)=x+3` and `g(x)=2x`, find `g(f(1))`.
<details><summary>Solution</summary>`f(1)=4`, `g(4)=8`.</details>

---
← [Algebra & Equations](../1-algebra-and-functions/01-algebra-equations.md)  |  [Exponents & Logarithms](../2-exponents-logs-and-sums/03-exponents-logarithms.md) →
