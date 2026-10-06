# Context Windows

*📓 Notes · [10 · LLM Mathematics](../README.md) · similarity context inference*

**📝 In simple words:** The maximum number of tokens the model can attend to at once.

**Why it costs so much:** attention builds an `n × n` score matrix, so cost grows with `n²`.

**✏️ Let me calculate it:** `n = 1,000` → 1,000,000 scores per head per layer; `n = 2,000` → 4,000,000 (**4×** for 2× the text).

**🤖 Why AI uses it:** it's the practical limit on how much text the model can "see"; long-context work is largely about making this cheaper.

```python
for n in (1000, 2000, 4000): print(n, n * n)
```

**🧪 Try it myself:** Tripling the context multiplies attention cost by? <details><summary>Solution</summary>9.</details>

---
← [Embedding Similarity](../3-similarity-context-inference/07-embedding-similarity.md)  |  [Basic LLM Inference Mathematics](../3-similarity-context-inference/09-basic-llm-inference-mathematics.md) →
