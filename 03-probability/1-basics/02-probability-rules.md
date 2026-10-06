# Probability Rules

*📓 Notes · [03 · Probability](../README.md) · basics*

**📝 In simple words:** How to combine probabilities.

**📐 Formula to remember:**

```text
P(not A)    = 1 − P(A)
P(A or B)   = P(A) + P(B) − P(A and B)
P(A and B)  = P(A) · P(B)        (if independent)
```

**🔢 Small example:** two fair coins: `P(both heads) = 0.5 · 0.5 = 0.25`.

**✏️ Let me calculate it:** `P(at least one head) = 1 − P(no heads) = 1 − 0.25 = 0.75`.

**🤖 Why AI uses it:** a sentence's probability is a product of word probabilities; "at least one" tricks show up in evaluation (pass@k).

```python
print(1 - 0.5**2)   # 0.75
```

**🧪 Try it myself:** P(no six in 3 die rolls)? <details><summary>Solution</summary>`(5/6)³ ≈ 0.579`.</details>

---
← [Random Variables](../1-basics/01-random-variables.md)  |  [Conditional Probability](../2-conditional-and-bayes/03-conditional-probability.md) →
