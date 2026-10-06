# 08 · Neural Network Mathematics

**The big idea:** a neural network is `y = f(Wx + b)` repeated. Training = forward pass, measure loss, backprop (chain rule), update weights.

**Where this leads →** a Transformer is the same pieces with attention added (09).

---

## 📂 Notes in this chapter

One short note per concept, grouped into folders. Read in order. Code builds on earlier notes, so `notebook.ipynb` (all code, in order) is the easiest way to run everything.

### `1-neuron-layers-forward/`

- [1. The Neuron & Weighted Sum](1-neuron-layers-forward/01-the-neuron-weighted-sum.md)
- [2. Activation Functions](1-neuron-layers-forward/02-activation-functions.md)
- [3. Forward Propagation](1-neuron-layers-forward/03-forward-propagation.md)

### `2-loss-and-backprop/`

- [4. Loss](2-loss-and-backprop/04-loss.md)
- [5. Backpropagation & the Chain Rule](2-loss-and-backprop/05-backpropagation-the-chain-rule.md)

### `3-updates-and-training-loop/`

- [6. Weight Updates](3-updates-and-training-loop/06-weight-updates.md)
- [7. The Training Loop](3-updates-and-training-loop/07-the-training-loop.md)
