# Why This Shows Up in ML and LLMs

*📓 Notes · [06 · Information Theory](../README.md) · mutual info and why*

```text
 Entropy H(p)          = unavoidable uncertainty of the data
 Cross-entropy H(p,q)  = what the model actually pays
 KL(p‖q)               = H(p,q) − H(p)  = the model's avoidable mistake
```

- Training an LLM minimizes next-token cross-entropy → makes `q` close to the true text distribution.
- **Perplexity** `= e^(cross-entropy)`: "how many choices the model is effectively torn between" (chapter 10).
- Temperature/sampling change the entropy of the output distribution.

---
← [Mutual Information](../3-mutual-info-and-why/05-mutual-information.md)
