# 06 · Information Theory

**The big idea:** how do we measure *surprise*, and how wrong a probability guess is? That's exactly what a classification or language-model loss needs.

**Where this leads →** cross-entropy loss (07), the LM training objective and perplexity (10).

> Logs below use base 2 (bits) for friendliness. ML code uses natural log (nats); the only difference is a constant factor.

---

## 📂 Notes in this chapter

One short note per concept, grouped into folders. Read in order. Code builds on earlier notes, so `notebook.ipynb` (all code, in order) is the easiest way to run everything.

### `1-surprise-and-entropy/`

- [1. Information (Surprise)](1-surprise-and-entropy/01-information-surprise.md)
- [2. Entropy](1-surprise-and-entropy/02-entropy.md)

### `2-comparing-distributions/`

- [3. Cross-Entropy](2-comparing-distributions/03-cross-entropy.md)
- [4. KL Divergence](2-comparing-distributions/04-kl-divergence.md)

### `3-mutual-info-and-why/`

- [5. Mutual Information](3-mutual-info-and-why/05-mutual-information.md)
- [6. Why This Shows Up in ML and LLMs](3-mutual-info-and-why/06-why-this-shows-up-in-ml-and-llms.md)
