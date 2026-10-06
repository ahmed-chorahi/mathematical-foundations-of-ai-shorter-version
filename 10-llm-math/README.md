# 10 · LLM Mathematics

**The big idea:** an LLM is a function from "text so far" to a probability distribution over the next token. Everything else (training loss, perplexity, sampling) is math on that distribution.

---

## 📂 Notes in this chapter

One short note per concept, grouped into folders. Read in order. Code builds on earlier notes, so `notebook.ipynb` (all code, in order) is the easiest way to run everything.

### `1-probability-and-loss/`

- [1. Language-Model Probability](1-probability-and-loss/01-language-model-probability.md)
- [2. Next-Token Prediction](1-probability-and-loss/02-next-token-prediction.md)
- [3. Cross-Entropy Objective & Log-Likelihood](1-probability-and-loss/03-cross-entropy-objective-log-likelihood.md)
- [4. Perplexity](1-probability-and-loss/04-perplexity.md)

### `2-sampling/`

- [5. Sampling & Temperature](2-sampling/05-sampling-temperature.md)
- [6. Top-k and Top-p (Nucleus)](2-sampling/06-top-k-and-top-p-nucleus.md)

### `3-similarity-context-inference/`

- [7. Embedding Similarity](3-similarity-context-inference/07-embedding-similarity.md)
- [8. Context Windows](3-similarity-context-inference/08-context-windows.md)
- [9. Basic LLM Inference Mathematics](3-similarity-context-inference/09-basic-llm-inference-mathematics.md)

---
**Full loop of the course:** vectors → matrices → gradients → probability → cross-entropy → softmax → attention → next-token prediction. 🎉
