# Conditional Probability

*📓 Notes · [03 · Probability](../README.md) · conditional and bayes*

**📝 In simple words:** Probability of A *given* that B happened.

**💡 Think of it like this:** Shrink the world to only cases where B is true.

**🔢 Small example:** 100 emails: 40 spam. 30 spam emails contain "free"; 10 non-spam contain "free".

**📐 Formula to remember:** `P(A|B) = P(A and B) / P(B)`

**✏️ Let me calculate it:** `P(spam | "free") = 30 / (30+10) = 0.75`.

**🤖 Why AI uses it:** a language model is literally `P(next word | previous words)`.

```python
print(30 / (30 + 10))   # 0.75
```

**🧪 Try it myself:** If 20 of the 60 non-spam emails contain "hello" and 10 of the 40 spam do, what's `P(spam | "hello")`? <details><summary>Solution</summary>`10 / 30 = 1/3`.</details>

---
← [Probability Rules](../1-basics/02-probability-rules.md)  |  [Bayes' Theorem](../2-conditional-and-bayes/04-bayes-theorem.md) →
