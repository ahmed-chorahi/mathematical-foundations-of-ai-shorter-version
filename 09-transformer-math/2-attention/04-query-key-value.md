# Query, Key, Value

*📓 Notes · [09 · Transformer Mathematics](../README.md) · attention*

**📝 In simple words:** Three different "views" of each token: `Q = XW_Q`, `K = XW_K`, `V = XW_V`.

**Intuition (library analogy):** Query = what I'm looking for. Key = what each book's label says. Value = the content I read once matched.

**📐 Formula to remember:** `Q = X W_Q`, `K = X W_K`, `V = X W_V`, with `W ∈ ℝ^(d×d_k)` learned.

**🤖 Why AI uses it:** separating "what to match on" from "what to pass along" makes attention flexible.

```python
d = 4; rng = np.random.default_rng(1)
Wq, Wk, Wv = (rng.normal(size=(d, d)) for _ in range(3))
Q, K, V = X @ Wq, X @ Wk, X @ Wv
print(Q.shape, K.shape, V.shape)   # (3,4) each
```

**🧪 Try it myself:** Shape of `Q` for 10 tokens, `d=512`, `d_k=64`? <details><summary>Solution</summary>`(10, 64)`.</details>

---
← [Positional Encoding](../1-inputs/03-positional-encoding.md)  |  [Dot-Product Attention, Scaling & Softmax](../2-attention/05-dot-product-attention-scaling-softmax.md) →
