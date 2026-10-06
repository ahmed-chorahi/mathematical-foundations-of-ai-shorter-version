# KL Divergence

*📓 Notes · [06 · Information Theory](../README.md) · comparing distributions*

**📝 In simple words:** The extra cost of using `q` when the truth is `p`; a "distance" between distributions (not symmetric).

**📐 Formula to remember:** `KL(p‖q) = Σ pᵢ log(pᵢ/qᵢ) = H(p, q) − H(p)`

**🔢 Small example:** `p = [0.5, 0.5]`, `q = [0.9, 0.1]`.

**✏️ Let me calculate it:** `H(p) = 1`, `H(p,q) = −0.5log₂0.9 − 0.5log₂0.1 = 0.076 + 1.661 = 1.737` → `KL = 0.737` bits.

**🤖 Why AI uses it:** minimizing cross-entropy = minimizing KL, since `H(p)` is fixed. KL also appears in VAEs, RLHF (keeping a fine-tuned model near the original), and distillation.

```python
p = np.array([0.5, 0.5]); q = np.array([0.9, 0.1])
print(np.sum(p * np.log2(p / q)))             # 0.737
```

**🧪 Try it myself:** `KL(p‖p)`? <details><summary>Solution</summary>0. Identical distributions.</details>

---
← [Cross-Entropy](../2-comparing-distributions/03-cross-entropy.md)  |  [Mutual Information](../3-mutual-info-and-why/05-mutual-information.md) →
