# Bias–Variance Intuition

*📓 Notes · [07 · Machine Learning Mathematics](../README.md) · pca and generalization*

**📝 In simple words:** Error = bias² + variance + noise.
- **High bias** (too simple) → underfits: misses the pattern.
- **High variance** (too flexible) → overfits: memorizes noise.

```text
 error
   │\                 /   test
   │ \               /
   │  \___________  /
   │   train   ↘ __/
   └─────────────────► model complexity
    underfit   sweet spot   overfit
```

**🤖 Why AI uses it:** explains train/test gaps; regularization, more data, and early stopping all fight variance.

```python
rng = np.random.default_rng(0)
f = lambda x: np.sin(2*np.pi*x)
xt = rng.uniform(0, 1, 20); yt = f(xt) + rng.normal(0, 0.2, 20)
xs = rng.uniform(0, 1, 200); ys = f(xs) + rng.normal(0, 0.2, 200)
for deg in (1, 3, 9):
    c = np.polyfit(xt, yt, deg)
    print(deg, np.mean((np.polyval(c, xt)-yt)**2).round(3), np.mean((np.polyval(c, xs)-ys)**2).round(3))
# degree 1: both high | 3: both low | 9: train tiny, test larger
```

**🧪 Try it myself:** Train error 0.01, test error 0.9: bias or variance problem? <details><summary>Solution</summary>Variance (overfitting).</details>

---
← [PCA (as an ML tool)](../4-pca-and-generalization/08-pca-as-an-ml-tool.md)
