# Top-k and Top-p (Nucleus)

*📓 Notes · [10 · LLM Mathematics](../README.md) · sampling*

**📝 In simple words:** Cut off the unlikely tail, renormalize, then sample.
- **Top-k:** keep the `k` most probable tokens.
- **Top-p:** keep the smallest set whose cumulative probability ≥ `p`.

**✏️ Let me calculate it (`p = [0.665, 0.245, 0.090]`):** top-k `k=2` → keep `0.665, 0.245` → divide by `0.910` → `[0.731, 0.269]`. Top-p `p=0.8`: cumulative `0.665 → 0.910 ≥ 0.8` → same two tokens.

**🤖 Why AI uses it:** stops rare, nonsensical tokens from being sampled while keeping variety.

```python
def top_k(p, k):
    q = np.zeros_like(p); idx = np.argsort(p)[-k:]; q[idx] = p[idx]; return q / q.sum()
def top_p(p, thr):
    order = np.argsort(p)[::-1]; cum = np.cumsum(p[order])
    keep = order[: np.searchsorted(cum, thr) + 1]
    q = np.zeros_like(p); q[keep] = p[keep]; return q / q.sum()
print(top_k(p, 2).round(3), top_p(p, 0.8).round(3))
```

**🧪 Try it myself:** Top-p with `p=0.6` on the distribution above? <details><summary>Solution</summary>Only the first token is needed (0.665 ≥ 0.6) → `[1, 0, 0]`.</details>

---
← [Sampling & Temperature](../2-sampling/05-sampling-temperature.md)  |  [Embedding Similarity](../3-similarity-context-inference/07-embedding-similarity.md) →
