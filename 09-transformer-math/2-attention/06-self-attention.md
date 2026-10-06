# Self-Attention

*📓 Notes · [09 · Transformer Mathematics](../README.md) · attention*

**📝 In simple words:** Attention where `Q`, `K`, `V` all come from the *same* sequence.

**💡 Think of it like this:** In "The animal didn't cross because **it** was tired", the token "it" learns to attend to "animal".

**Causal mask (GPT-style):** a token can't peek at future tokens: set scores above the diagonal to `−∞` before softmax, so those weights become 0.

```python
def causal_attention(Q, K, V):
    s = Q @ K.T / np.sqrt(K.shape[-1])
    s = np.where(np.triu(np.ones_like(s), 1) == 1, -1e9, s)   # hide the future
    return softmax(s) @ V
print(causal_attention(Q, K, V).shape)   # (3, 4)
```

**🧪 Try it myself:** In a causal model with 3 tokens, how many attention weights are non-zero in total? <details><summary>Solution</summary>`1 + 2 + 3 = 6` (lower triangle).</details>

---
← [Dot-Product Attention, Scaling & Softmax](../2-attention/05-dot-product-attention-scaling-softmax.md)  |  [Multi-Head Attention](../3-multi-head-and-ffn/07-multi-head-attention.md) →
