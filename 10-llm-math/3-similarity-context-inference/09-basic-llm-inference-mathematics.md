# Basic LLM Inference Mathematics

*📓 Notes · [10 · LLM Mathematics](../README.md) · similarity context inference*

**Generation loop:** (1) run the model on the prompt → logits (2) pick a token (sampling) (3) append it (4) repeat.

**KV cache:** keys/values of earlier tokens don't change, so we store them instead of recomputing.

**Memory for the KV cache:** `2 × layers × tokens × d_model × bytes`.

**✏️ Let me calculate it:** 32 layers, `d_model = 4096`, 1,000 tokens, fp16 (2 bytes): `2·32·1000·4096·2 = 524,288,000 B ≈ 0.52 GB`.

**Compute per token:** roughly `2 × N` floating-point operations for `N` parameters: a 7B model ≈ 14 GFLOPs per generated token.

**Weights memory:** `N × bytes`: 7B in fp16 = 14 GB; in 4-bit ≈ 3.5 GB.

```python
layers, d, n, bytes_ = 32, 4096, 1000, 2
print(2 * layers * n * d * bytes_ / 1e9, "GB KV cache")
print(7e9 * 2 / 1e9, "GB of fp16 weights")
```

**🧪 Try it myself:** KV cache for the same model with 4,000 tokens? <details><summary>Solution</summary>4× larger ≈ 2.1 GB.</details>

---
← [Context Windows](../3-similarity-context-inference/08-context-windows.md)
