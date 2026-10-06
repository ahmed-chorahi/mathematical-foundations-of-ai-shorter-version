# Forward Propagation

*📓 Notes · [08 · Neural Network Mathematics](../README.md) · neuron layers forward*

**📝 In simple words:** Pushing the input through the layers to get a prediction.

**🔢 Small example:** one input `x=1`; hidden: `h = ReLU(2x) `; output `ŷ = 0.5h`.

**📐 Formula to remember:** `h = ReLU(W₁x + b₁)`, `ŷ = W₂h + b₂`

**✏️ Let me calculate it:** `h = ReLU(2) = 2`; `ŷ = 0.5·2 = 1`.

**🤖 Why AI uses it:** this is inference: what a trained model does every time you use it.

```python
x, w1, w2 = 1.0, 2.0, 0.5
h = max(0, w1 * x); y_hat = w2 * h
print(h, y_hat)   # 2.0 1.0
```

**🧪 Try it myself:** Same net with `x = −1`? <details><summary>Solution</summary>`h = ReLU(−2) = 0`, so `ŷ = 0`.</details>

---
← [Activation Functions](../1-neuron-layers-forward/02-activation-functions.md)  |  [Loss](../2-loss-and-backprop/04-loss.md) →
