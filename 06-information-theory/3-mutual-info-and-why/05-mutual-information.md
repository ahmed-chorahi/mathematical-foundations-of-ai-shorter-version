# Mutual Information

*📓 Notes · [06 · Information Theory](../README.md) · mutual info and why*

**📝 In simple words:** How much knowing one variable reduces uncertainty about another.

**📐 Formula to remember:** `I(X;Y) = Σ P(x,y) log[P(x,y) / (P(x)P(y))]`

**🔢 Small example:** joint `[[0.4, 0.1],[0.1, 0.4]]`. Marginals are 0.5 each.

**✏️ Let me calculate it:** `2·0.4·log₂(0.4/0.25) + 2·0.1·log₂(0.1/0.25) = 0.543 − 0.264 = 0.278` bits. Independent variables would give 0.

**🤖 Why AI uses it:** feature selection, representation learning (InfoNCE / contrastive losses).

```python
J = np.array([[0.4, 0.1], [0.1, 0.4]])
px, py = J.sum(1), J.sum(0)
print(np.sum(J * np.log2(J / np.outer(px, py))))   # 0.278
```

**🧪 Try it myself:** MI when `P(x,y) = P(x)P(y)`? <details><summary>Solution</summary>0 (`log 1 = 0`).</details>

---
← [KL Divergence](../2-comparing-distributions/04-kl-divergence.md)  |  [Why This Shows Up in ML and LLMs](../3-mutual-info-and-why/06-why-this-shows-up-in-ml-and-llms.md) →
