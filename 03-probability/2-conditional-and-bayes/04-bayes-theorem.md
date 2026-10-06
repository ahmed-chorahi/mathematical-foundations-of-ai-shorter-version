# Bayes' Theorem

*📓 Notes · [03 · Probability](../README.md) · conditional and bayes*

**📝 In simple words:** Flip a conditional: from `P(B|A)` to `P(A|B)`.

**💡 Think of it like this:** Update your belief after seeing evidence.

**🔢 Small example:** disease affects 1%. A test catches 90% of cases (sensitivity) and falsely flags 5% of healthy people.

**📐 Formula to remember:** `P(A|B) = P(B|A) P(A) / P(B)`

**✏️ Let me calculate it:**

```text
P(pos) = 0.9·0.01 + 0.05·0.99 = 0.009 + 0.0495 = 0.0585
P(disease | pos) = 0.009 / 0.0585 ≈ 0.154
```

Only 15%: the disease is rare, so most positives are false alarms.

**🤖 Why AI uses it:** Naive Bayes classifiers, probabilistic reasoning, and the "prior × likelihood" view of training (MLE vs MAP).

```python
p_d, sens, fpr = 0.01, 0.9, 0.05
p_pos = sens*p_d + fpr*(1 - p_d)
print(sens*p_d / p_pos)   # ≈ 0.154
```

**🧪 Try it myself:** Same test, but disease prevalence 10%? <details><summary>Solution</summary>`P(pos)=0.09+0.045=0.135`; `0.09/0.135 ≈ 0.667`.</details>

---
← [Conditional Probability](../2-conditional-and-bayes/03-conditional-probability.md)  |  [Expected Value](../3-expectation-variance-covariance/05-expected-value.md) →
