# 09 · Transformer Mathematics

**The big idea:** instead of reading words one at a time, let every token *look at* every other token and decide what matters. That "looking" is a softmax over dot products.

**Where this leads →** an LLM is a big stack of these blocks that predicts the next token (10).

```text
 tokens → embeddings (+ position) → [ Attention → Add&Norm → FFN → Add&Norm ] × N → logits
```

---

## 📂 Notes in this chapter

One short note per concept, grouped into folders. Read in order. Code builds on earlier notes, so `notebook.ipynb` (all code, in order) is the easiest way to run everything.

### `1-inputs/`

- [1. Token Representations](1-inputs/01-token-representations.md)
- [2. Embeddings](1-inputs/02-embeddings.md)
- [3. Positional Encoding](1-inputs/03-positional-encoding.md)

### `2-attention/`

- [4. Query, Key, Value](2-attention/04-query-key-value.md)
- [5. Dot-Product Attention, Scaling & Softmax](2-attention/05-dot-product-attention-scaling-softmax.md)
- [6. Self-Attention](2-attention/06-self-attention.md)

### `3-multi-head-and-ffn/`

- [7. Multi-Head Attention](3-multi-head-and-ffn/07-multi-head-attention.md)
- [8. Feed-Forward Network](3-multi-head-and-ffn/08-feed-forward-network.md)

### `4-stabilizers/`

- [9. Residual Connections](4-stabilizers/09-residual-connections.md)
- [10. Layer Normalization](4-stabilizers/10-layer-normalization.md)
