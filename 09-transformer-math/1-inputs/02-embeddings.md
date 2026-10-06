# Embeddings

*📓 Notes · [09 · Transformer Mathematics](../README.md) · inputs*

**📝 In simple words:** A lookup table: ID → learned vector.

**💡 Think of it like this:** Similar words end up with nearby vectors (dot product / cosine large).

**📐 Formula to remember:** `E ∈ ℝ^(V×d)`; embedding of token `i` is row `E[i]`.

**✏️ Let me calculate it:** vocab 20, d = 4 → `E` is `20×4`; ids `[4,17,9]` → a `3×4` matrix `X`.

**🤖 Why AI uses it:** gives the network a meaningful continuous space; the embedding table is learned by backprop like any weight.

```python
rng = np.random.default_rng(0)
E = rng.normal(size=(20, 4))
X = E[ids]; print(X.shape)   # (3, 4)
```

**🧪 Try it myself:** Vocab 50,000 and d=768: embedding table size? <details><summary>Solution</summary>`50,000 × 768 ≈ 38.4M` numbers.</details>

---
← [Token Representations](../1-inputs/01-token-representations.md)  |  [Positional Encoding](../1-inputs/03-positional-encoding.md) →
