# Binary Cross-Entropy

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · classification*

**📝 In simple words:** The loss for yes/no predictions (chapter 06's cross-entropy with 2 classes).

**📐 Formula to remember:** `BCE = −[y ln p + (1−y) ln(1−p)]`

**🔢 Small example:** `y = 1`.

**✏️ Let me calculate it:** `p = 0.9` → `−ln 0.9 = 0.105`. `p = 0.1` → `2.303`. For `y=[1,0]`, `p=[0.9,0.2]`: `(0.105 + 0.223)/2 = 0.164`.

**🤖 Why AI uses it:** every binary classifier, plus multi-label outputs.

```python
y = np.array([1, 0]); p = np.array([0.9, 0.2])
print(-np.mean(y*np.log(p) + (1-y)*np.log(1-p)))   # 0.164
```

**🧪 Try it myself:** `y=0`, `p=0.5`? <details><summary>Solution</summary>`−ln 0.5 = 0.693`.</details>

---
← [Logistic Regression & the Sigmoid](../2-classification/03-logistic-regression-the-sigmoid.md)  |  [Softmax](../2-classification/05-softmax.md) →
