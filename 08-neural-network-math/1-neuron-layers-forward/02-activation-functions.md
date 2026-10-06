# Activation Functions

*📓 Notes · [08 · Neural Network Mathematics](../README.md) · neuron layers forward*

**📝 In simple words:** A non-linear squash applied to `z`.

**💡 Think of it like this:** Without it, stacked layers collapse into one linear map (matrix × matrix = matrix). The bend lets networks learn curves.

| Name | Formula | Range | Used for |
|---|---|---|---|
| Sigmoid | `1/(1+e⁻ᶻ)` | (0,1) | binary output, gates |
| Tanh | `(eᶻ−e⁻ᶻ)/(eᶻ+e⁻ᶻ)` | (−1,1) | older RNNs |
| ReLU | `max(0, z)` | [0,∞) | hidden layers |
| GELU | `z·Φ(z)` (smooth ReLU) | ≈[−0.17,∞) | Transformers |

**✏️ Let me calculate it (`z = −1`):** sigmoid `0.269`, tanh `−0.762`, ReLU `0`.

```python
z = -1.0
print(1/(1+np.exp(-z)), np.tanh(z), max(0, z))
```

**🧪 Try it myself:** ReLU(3) and ReLU(−3)? <details><summary>Solution</summary>3 and 0.</details>

---
← [The Neuron & Weighted Sum](../1-neuron-layers-forward/01-the-neuron-weighted-sum.md)  |  [Forward Propagation](../1-neuron-layers-forward/03-forward-propagation.md) →
