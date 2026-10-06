# Loss

*📓 Notes · [08 · Neural Network Mathematics](../README.md) · loss and backprop*

**📝 In simple words:** Compare prediction to truth, one number out (chapter 05/07).

**🔢 Small example:** `y = 3`, `ŷ = 1` → `L = (ŷ − y)² = 4`.

**Softmax + cross-entropy gem:** for probabilities `p` and one-hot label `y`, the gradient of the loss with respect to the logits is just **`p − y`**. Example `p = [0.665, 0.245, 0.090]`, `y = [1,0,0]` → gradient `[−0.335, 0.245, 0.090]`: push class 1 up, others down.

```python
p = np.array([0.665, 0.245, 0.090]); y = np.array([1, 0, 0])
print(p - y)
```

**🧪 Try it myself:** `p=[0.2, 0.8]`, `y=[0,1]`: gradient? <details><summary>Solution</summary>`[0.2, −0.2]`.</details>

---
← [Forward Propagation](../1-neuron-layers-forward/03-forward-propagation.md)  |  [Backpropagation & the Chain Rule](../2-loss-and-backprop/05-backpropagation-the-chain-rule.md) →
