# Multi-Head Attention

*📓 Notes · [09 · Transformer Mathematics](../README.md) · multi head and ffn*

**📝 In simple words:** Run several attentions in parallel on smaller slices, then glue the results together.

**💡 Think of it like this:** One head might track grammar, another coreference, another position.

**📐 Formula to remember:** `head_i = Attention(XW_Qⁱ, XW_Kⁱ, XW_Vⁱ)`; `MHA = Concat(head₁..head_h) W_O`, with `d_k = d_model / h`.

**✏️ Let me calculate it:** `d_model = 4`, `h = 2` → each head works in 2 dims → concat back to 4.

```python
h, dk = 2, 2
heads = [attention(Q[:, i*dk:(i+1)*dk], K[:, i*dk:(i+1)*dk], V[:, i*dk:(i+1)*dk]) for i in range(h)]
Wo = rng.normal(size=(4, 4))
out = np.concatenate(heads, axis=-1) @ Wo; print(out.shape)   # (3, 4)
```

**🧪 Try it myself:** `d_model=768`, 12 heads: `d_k`? <details><summary>Solution</summary>64.</details>

---
← [Self-Attention](../2-attention/06-self-attention.md)  |  [Feed-Forward Network](../3-multi-head-and-ffn/08-feed-forward-network.md) →
