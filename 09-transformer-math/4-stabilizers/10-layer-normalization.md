# Layer Normalization

*📓 Notes · [09 · Transformer Mathematics](../README.md) · stabilizers*

**📝 In simple words:** Standardize each token's vector, then re-scale with learned `γ`, `β`.

**📐 Formula to remember:** `LN(x) = γ · (x − μ)/√(σ² + ε) + β`

**🔢 Small example:** `x = [1, 2, 3]`.

**✏️ Let me calculate it:** `μ = 2`, `σ² = 2/3`, `σ = 0.816` → `[−1.225, 0, 1.225]`.

**🤖 Why AI uses it:** keeps activations in a stable range so training doesn't explode or stall.

```python
def layer_norm(x, eps=1e-5):
    return (x - x.mean(-1, keepdims=True)) / np.sqrt(x.var(-1, keepdims=True) + eps)
print(layer_norm(np.array([1., 2., 3.])).round(3))   # [-1.225 0. 1.225]
```

**Putting it together (one block):**

```python
def block(x):
    x = layer_norm(x + causal_attention(x @ Wq, x @ Wk, x @ Wv))
    return layer_norm(x + ffn(x))
print(block(X).shape)   # (3, 4)
```

**🧪 Try it myself:** What is the mean of a layer-normed vector? <details><summary>Solution</summary>0 (before `γ`, `β`).</details>

---
← [Residual Connections](../4-stabilizers/09-residual-connections.md)
