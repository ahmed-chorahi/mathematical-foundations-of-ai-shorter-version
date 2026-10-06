# Feed-Forward Network

*📓 Notes · [09 · Transformer Mathematics](../README.md) · multi head and ffn*

**📝 In simple words:** The same small 2-layer MLP applied to each token separately.

**📐 Formula to remember:** `FFN(x) = W₂ · act(W₁x + b₁) + b₂`, with hidden size usually `4·d_model`.

**🤖 Why AI uses it:** attention *mixes* information between tokens; the FFN *processes* each token (much of the model's stored knowledge sits here).

```python
W1 = rng.normal(size=(4, 16)); W2 = rng.normal(size=(16, 4))
ffn = lambda x: np.maximum(0, x @ W1) @ W2
print(ffn(out).shape)   # (3, 4)
```

**🧪 Try it myself:** Parameters in an FFN with `d=512`, hidden `2048` (ignore biases)? <details><summary>Solution</summary>`2·512·2048 ≈ 2.1M`.</details>

---
← [Multi-Head Attention](../3-multi-head-and-ffn/07-multi-head-attention.md)  |  [Residual Connections](../4-stabilizers/09-residual-connections.md) →
