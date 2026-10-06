# Residual Connections

*📓 Notes · [09 · Transformer Mathematics](../README.md) · stabilizers*

**📝 In simple words:** Add the input back: `y = x + F(x)`.

**💡 Think of it like this:** The block only has to learn a *correction*. The gradient has a clean shortcut: `∂y/∂x = 1 + ∂F/∂x`, so it never vanishes through the "1".

**🤖 Why AI uses it:** makes 100-layer networks trainable.

```python
y = X + out        # residual around attention
```

**🧪 Try it myself:** If `F(x) = 0`, what does the block do? <details><summary>Solution</summary>Passes `x` through unchanged (identity).</details>

---
← [Feed-Forward Network](../3-multi-head-and-ffn/08-feed-forward-network.md)  |  [Layer Normalization](../4-stabilizers/10-layer-normalization.md) →
