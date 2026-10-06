# Cross-Entropy

*📓 Notes · [06 · Information Theory](../README.md) · comparing distributions*

**📝 In simple words:** The average surprise when the truth follows `p` but you *predicted* `q`.

**📐 Formula to remember:** `H(p, q) = −Σ pᵢ log qᵢ`

**🔢 Small example:** true label is class 1 (`p = [1, 0]`). Model says `q = [0.7, 0.3]`.

**✏️ Let me calculate it:** `−(1·ln 0.7 + 0·ln 0.3) = −ln 0.7 = 0.357` nats. If the model said `0.99` → `0.010`. If it said `0.01` → `4.6`. Confident and wrong gets punished hard.

**🤖 Why AI uses it:** it's *the* classification loss, and the LLM training loss (next-token cross-entropy).

```python
p = np.array([1, 0]); q = np.array([0.7, 0.3])
print(-np.sum(p * np.log(q)))                 # 0.357
for c in (0.99, 0.5, 0.01): print(c, -np.log(c))
```

**🧪 Try it myself:** True class prob predicted as 0.5. Loss (nats)? <details><summary>Solution</summary>`−ln 0.5 = 0.693`.</details>

---
← [Entropy](../1-surprise-and-entropy/02-entropy.md)  |  [KL Divergence](../2-comparing-distributions/04-kl-divergence.md) →
