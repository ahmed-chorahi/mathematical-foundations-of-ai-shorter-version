# The Training Loop

*📓 Notes · [08 · Neural Network Mathematics](../README.md) · updates and training loop*

```text
repeat:
  1. forward pass     → predictions
  2. loss             → how wrong
  3. backward pass    → gradients
  4. update weights   → w ← w − α·grad
```

A complete tiny network learning XOR (a problem no single line can solve), manual gradients only:

```python
rng = np.random.default_rng(1)
X = np.array([[0,0],[0,1],[1,0],[1,1]], float); Y = np.array([[0],[1],[1],[0]], float)
W1 = rng.normal(0, 1, (2, 4)); b1 = np.zeros(4)
W2 = rng.normal(0, 1, (4, 1)); b2 = np.zeros(1)
sig = lambda z: 1/(1+np.exp(-z))
for step in range(5000):
    H = np.tanh(X @ W1 + b1)                 # forward
    P = sig(H @ W2 + b2)
    loss = -np.mean(Y*np.log(P) + (1-Y)*np.log(1-P))
    dZ2 = (P - Y) / len(X)                   # backward (BCE + sigmoid → p − y)
    dW2 = H.T @ dZ2; db2 = dZ2.sum(0)
    dH = dZ2 @ W2.T; dZ1 = dH * (1 - H**2)   # tanh′ = 1 − tanh²
    dW1 = X.T @ dZ1; db1 = dZ1.sum(0)
    for p_, g in ((W1, dW1), (b1, db1), (W2, dW2), (b2, db2)):
        p_ -= 0.5 * g                        # update
print(round(loss, 4), P.round(2).ravel())    # loss ≈ 0.001, predictions ≈ [0 1 1 0]
# try seed 0: it gets stuck at loss 0.35. Bad starting weights can trap training!
```

**🧪 Try it myself:** In the loop, which line is "backprop"? <details><summary>Solution</summary>From `dZ2 = ...` to `db1 = ...`. These apply the chain rule layer by layer.</details>

---
← [Weight Updates](../3-updates-and-training-loop/06-weight-updates.md)
