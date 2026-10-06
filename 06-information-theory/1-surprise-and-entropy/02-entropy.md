# Entropy

*📓 Notes · [06 · Information Theory](../README.md) · surprise and entropy*

**📝 In simple words:** The *average* surprise of a distribution, i.e. its uncertainty.

**📐 Formula to remember:** `H(p) = −Σ pᵢ log₂ pᵢ`

**🔢 Small example:** fair coin vs biased coin (0.9 / 0.1).

**✏️ Let me calculate it:**

```text
fair:   −(0.5·log₂0.5 + 0.5·log₂0.5) = 1 bit
biased: −(0.9·log₂0.9 + 0.1·log₂0.1) = 0.137 + 0.332 = 0.469 bits
```

Fair = most unpredictable. Certain outcome = 0 bits.

**🤖 Why AI uses it:** entropy of a model's output tells how unsure it is; it's the lower bound on how well any model can predict.

```python
H = lambda p: -np.sum(p * np.log2(p))
print(H(np.array([0.5, 0.5])), H(np.array([0.9, 0.1])))   # 1.0  0.469
```

**🧪 Try it myself:** Entropy of a fair 4-sided die? <details><summary>Solution</summary>`−4·(¼·log₂¼) = 2` bits.</details>

---
← [Information (Surprise)](../1-surprise-and-entropy/01-information-surprise.md)  |  [Cross-Entropy](../2-comparing-distributions/03-cross-entropy.md) →
