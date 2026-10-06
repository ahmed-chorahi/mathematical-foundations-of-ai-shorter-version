# Sampling & Temperature

*📓 Notes · [10 · LLM Mathematics](../README.md) · sampling*

**📝 In simple words:** Pick the next token from `p`; temperature reshapes `p` first.

**📐 Formula to remember:** `pᵢ = softmax(zᵢ / T)`

**✏️ Let me calculate it (`z = [2,1,0]`):**

```text
T = 0.5 → z/T=[4,2,0] → [0.867, 0.117, 0.016]   sharper, safer
T = 1   →            → [0.665, 0.245, 0.090]
T = 2   → [1,0.5,0]  → [0.506, 0.307, 0.186]   flatter, more creative
T → 0   → always the top token (greedy)
```

**🤖 Why AI uses it:** controls the creativity/reliability trade-off (it changes the *entropy* of the output, 06).

```python
z = np.array([2., 1., 0.])
for T in (0.5, 1, 2): print(T, softmax(z / T).round(3))
rng = np.random.default_rng(0)
print(rng.choice(["cat", "dog", "car"], p=softmax(z)))
```

**🧪 Try it myself:** What does T = 1 do to the distribution? <details><summary>Solution</summary>Nothing. It's the plain softmax.</details>

---
← [Perplexity](../1-probability-and-loss/04-perplexity.md)  |  [Top-k and Top-p (Nucleus)](../2-sampling/06-top-k-and-top-p-nucleus.md) →
