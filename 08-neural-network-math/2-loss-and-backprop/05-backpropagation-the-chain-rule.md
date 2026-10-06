# Backpropagation & the Chain Rule

*📓 Notes · [08 · Neural Network Mathematics](../README.md) · loss and backprop*

**📝 In simple words:** Computing every weight's gradient by walking backward through the network.

**💡 Think of it like this:** The loss blames the output; the output blames the layer before it, and so on. Each blame is a multiplication of local slopes: the chain rule (02).

**📐 Formula to remember:** `∂L/∂w₁ = ∂L/∂ŷ · ∂ŷ/∂h · ∂h/∂w₁`

**🔢 Small example:** the net from step 3 with `y = 3`, so `L = (ŷ − y)²`.

**✏️ Let me calculate it:**

```text
forward:  h = 2,  ŷ = 1,  L = (1−3)² = 4
∂L/∂ŷ  = 2(ŷ − y)     = −4
∂L/∂w₂ = ∂L/∂ŷ · h    = −4 · 2   = −8
∂L/∂h  = ∂L/∂ŷ · w₂   = −4 · 0.5 = −2
∂L/∂w₁ = ∂L/∂h · 1(ReLU′, since z>0) · x = −2
```

**🤖 Why AI uses it:** this is how *every* deep network learns, from LeNet to GPT.

```python
x, y, w1, w2 = 1.0, 3.0, 2.0, 0.5
h = max(0, w1*x); y_hat = w2*h
dL_dyh = 2*(y_hat - y)
dw2 = dL_dyh * h
dw1 = dL_dyh * w2 * (1.0 if w1*x > 0 else 0.0) * x
print(dw1, dw2)   # -2.0 -8.0
# gradient check: nudge and measure
def L(w1, w2): return (w2*max(0, w1*x) - y)**2
print((L(w1+1e-6, w2) - L(w1, w2)) / 1e-6)   # ≈ -2
```

**🧪 Try it myself:** Why is gradient 0 for a ReLU unit whose `z < 0`? <details><summary>Solution</summary>ReLU′ is 0 there, so the product is 0 and the weight gets no signal ("dead ReLU").</details>

---
← [Loss](../2-loss-and-backprop/04-loss.md)  |  [Weight Updates](../3-updates-and-training-loop/06-weight-updates.md) →
