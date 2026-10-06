# Dot-Product Attention, Scaling & Softmax

*📓 Notes · [09 · Transformer Mathematics](../README.md) · attention*

**📝 In simple words:** Score every token pair with a dot product, softmax into weights, then average the values.

**📐 Formula to remember:** `Attention(Q,K,V) = softmax(QKᵀ / √d_k) V`

**🔢 Small example (2 tokens, d=2):** `Q = K = I`, `V = [[1,2],[3,4]]`.

**✏️ Let me calculate it:**

```text
QKᵀ = [[1,0],[0,1]]  → divide by √2 → [[0.707, 0],[0, 0.707]]
softmax row 1: e^0.707=2.028, e^0=1 → [0.670, 0.330]
output row 1 = 0.670·[1,2] + 0.330·[3,4] = [1.660, 2.660]
output row 2 = [2.340, 3.340]
```

**Why scale by √d_k?** If entries of `q` and `k` have variance 1, `q·k` has variance `d_k`. Big scores make softmax nearly one-hot with tiny gradients, so dividing by `√d_k` keeps variance ≈ 1.

```python
def softmax(z):
    e = np.exp(z - z.max(-1, keepdims=True)); return e / e.sum(-1, keepdims=True)
def attention(Q, K, V):
    return softmax(Q @ K.T / np.sqrt(K.shape[-1])) @ V
I = np.eye(2); V2 = np.array([[1., 2.], [3., 4.]])
print(attention(I, I, V2).round(3))   # [[1.66 2.66] [2.34 3.34]]
```

**🧪 Try it myself:** If all scores are equal, what are the attention weights over 4 tokens? <details><summary>Solution</summary>`[0.25, 0.25, 0.25, 0.25]`: a plain average.</details>

---
← [Query, Key, Value](../2-attention/04-query-key-value.md)  |  [Self-Attention](../2-attention/06-self-attention.md) →
