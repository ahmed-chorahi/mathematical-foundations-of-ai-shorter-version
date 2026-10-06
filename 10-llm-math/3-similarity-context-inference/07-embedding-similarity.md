# Embedding Similarity

*📓 Notes · [10 · LLM Mathematics](../README.md) · similarity context inference*

**📝 In simple words:** Meaning compared by cosine similarity between vectors (01).

**📐 Formula to remember:** `cos(a,b) = a·b / (‖a‖‖b‖)`

**🔢 Small example:** `king=[0.9,0.1]`, `queen=[0.8,0.3]`, `apple=[0.1,0.9]`.

**✏️ Let me calculate it:** `cos(king,queen) = 0.75/(0.906·0.854) = 0.97`; `cos(king,apple) = 0.18/(0.906·0.906) = 0.22`.

**🤖 Why AI uses it:** semantic search and retrieval (RAG) find the nearest embeddings to a query.

```python
cos = lambda a, b: a @ b / (np.linalg.norm(a) * np.linalg.norm(b))
king, queen, apple = np.array([.9, .1]), np.array([.8, .3]), np.array([.1, .9])
print(cos(king, queen).round(2), cos(king, apple).round(2))   # 0.97 0.22
```

**🧪 Try it myself:** Cosine similarity of a vector with itself? <details><summary>Solution</summary>1.</details>

---
← [Top-k and Top-p (Nucleus)](../2-sampling/06-top-k-and-top-p-nucleus.md)  |  [Context Windows](../3-similarity-context-inference/08-context-windows.md) →
