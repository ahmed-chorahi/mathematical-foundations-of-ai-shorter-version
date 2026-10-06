# Positional Encoding

*📓 Notes · [09 · Transformer Mathematics](../README.md) · inputs*

**📝 In simple words:** Extra numbers added to say *where* a token is.

**💡 Think of it like this:** Attention itself ignores order ("dog bites man" = "man bites dog" as a set). Position info fixes this.

**📐 Formula to remember (sinusoidal):** `PE(pos, 2i) = sin(pos / 10000^(2i/d))`, `PE(pos, 2i+1) = cos(pos / 10000^(2i/d))`

**✏️ Let me calculate it (d=4, pos=1):** `i=0`: `sin(1)=0.841`, `cos(1)=0.540`; `i=1`: divisor `100` → `sin(0.01)=0.010`, `cos(0.01)=1.000` → `[0.841, 0.540, 0.010, 1.000]`.

**🤖 Why AI uses it:** order matters in language. (Modern LLMs often use rotary/learned positions, same goal.)

```python
def pos_enc(n, d):
    pe = np.zeros((n, d))
    pos = np.arange(n)[:, None]; i = np.arange(0, d, 2)
    pe[:, 0::2] = np.sin(pos / 10000**(i/d)); pe[:, 1::2] = np.cos(pos / 10000**(i/d))
    return pe
print(pos_enc(3, 4)[1].round(3))   # [0.841 0.54 0.01 1.]
X = X + pos_enc(3, 4)
```

**🧪 Try it myself:** What is `PE(0, ·)`? <details><summary>Solution</summary>`sin(0)=0`, `cos(0)=1` → `[0,1,0,1]`.</details>

---
← [Embeddings](../1-inputs/02-embeddings.md)  |  [Query, Key, Value](../2-attention/04-query-key-value.md) →
