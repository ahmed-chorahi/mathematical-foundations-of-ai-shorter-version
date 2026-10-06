<div align="center">

# 🧮 Mathematical Foundations of AI

**I'm learning the math behind AI from the ground up, and writing it down as I go.**

`Basic Math → Linear Algebra → Calculus → Probability → Statistics → Optimization → Information Theory → ML → Neural Networks → Transformers → LLMs`

</div>

---

## What is this repository?

A step-by-step personal learning repo. Each folder is one stage of the journey, written the way I wish someone had explained it to me: small numbers, real examples, tiny Python snippets, and a practice question at the end of every concept.

It is **not** a textbook. There are no long proofs. If a concept doesn't help me understand AI, it isn't here.

## Why I created it

I kept seeing `softmax`, `cross-entropy`, `∇L`, and `QKᵀ/√d` in ML courses and papers, and using them without really *seeing* them. This repo is me closing that gap, one concept at a time, and keeping notes that future-me (and maybe you) can reuse.

## Learning philosophy

1. **Why before how.** Every concept ends with *"Why AI needs it"*.
2. **Small numbers first.** If I can't do it by hand with 2 or 3 numbers, I don't understand it yet.
3. **Manual first, library second.** Write the math with NumPy, *then* compare with the library version.
4. **Practice or it didn't happen.** One question per concept, with a solution.
5. **Connect it forward.** Each idea points to where it shows up later (attention is just dot products!).

Every concept follows the same pattern:

```text
What is it? → Intuition → Small example → Formula → Step by step
          → Why AI needs it → Tiny Python → Practice → Solution
```

## Roadmap & progress

Update the boxes as you go. See [ROADMAP.md](ROADMAP.md) for the details and [CONNECTIONS.md](CONNECTIONS.md) for how everything links.

- [x] [00 — Prerequisites](00-prerequisites/): algebra, functions, logs, summation, geometry, notation
- [x] [01 — Linear Algebra](01-linear-algebra/): vectors, matrices, eigen, PCA, SVD
- [x] [02 — Calculus](02-calculus/): derivatives, gradients, chain rule, Jacobian, Hessian
- [x] [03 — Probability](03-probability/): Bayes, expectation, distributions
- [x] [04 — Statistics](04-statistics/): variance, confidence intervals, p-values
- [x] [05 — Optimization](05-optimization/): gradient descent, SGD, momentum, Adam
- [x] [06 — Information Theory](06-information-theory/): entropy, cross-entropy, KL
- [x] [07 — Machine Learning Math](07-machine-learning-math/): regression, softmax, MLE, regularization
- [x] [08 — Neural Network Math](08-neural-network-math/): forward pass, backprop, training loop
- [x] [09 — Transformer Math](09-transformer-math/): embeddings, attention, multi-head, LayerNorm
- [x] [10 — LLM Math](10-llm-math/): perplexity, sampling, temperature, inference

> Tip: tick these boxes yourself as you finish each chapter. Learning is more fun when you can see progress.

## From math to LLMs

```text
 Vectors & Matrices ──► Dot products ─────────────────────────┐
        │                                                      ▼
 Derivatives & Chain rule ──► Gradient descent ──► Backprop ──► Neural networks
        │                                                      │
 Probability ──► Entropy / Cross-entropy ──► Loss functions ───┤
                                                               ▼
                         Embeddings ──► Attention ──► Transformers ──► LLMs
```

| Stage | Key math | Where it shows up |
|---|---|---|
| ML | least squares, MLE, regularization | regression, classification |
| Deep learning | matrix multiply, chain rule | layers, backprop |
| Transformers | dot product, softmax, normalization | attention, LayerNorm |
| LLMs | conditional probability, cross-entropy | next-token loss, sampling |

## Tools used

- **Python 3**, **NumPy** for the math, **Matplotlib** for pictures
- **Jupyter** notebooks (each chapter has `notebook.ipynb` built from its README)
- Nothing else. No hidden frameworks.

## How the notes are organised

Every concept has its own small note file, like a page in a student's notebook. Chapters are folders, related concepts are grouped in numbered subfolders:

```text
05-optimization/
├── README.md                      ← chapter intro + index of all notes
├── notebook.ipynb                 ← all the chapter's code, in order
├── 1-what-to-minimize/
│   ├── 01-objective-loss-functions.md
│   └── 02-local-vs-global-minima.md
├── 2-gradient-descent-family/
│   ├── 03-gradient-descent.md
│   ├── 04-learning-rate.md
│   └── 05-sgd-mini-batch-gradient-descent.md
└── ...
```

Each note uses the same labels: 📝 In simple words · 💡 Think of it like this · 🔢 Small example · 📐 Formula to remember · ✏️ Let me calculate it · 🤖 Why AI uses it · 🧪 Try it myself.

## How to use this repo

```bash
git clone https://github.com/<your-username>/mathematical-foundations-of-ai.git
cd mathematical-foundations-of-ai
pip install -r requirements.txt
jupyter notebook          # open any chapter's notebook.ipynb
```

1. Go through the folders **in order** (00 → 10).
2. Read the README, type the code yourself, and try the practice question before opening the solution.
3. Re-generate notebooks after editing a README: `python tools/build_notebooks.py` (add `--check` to run all the code).
4. Stuck? Check [CONNECTIONS.md](CONNECTIONS.md) to see what the concept is built from.

---
<div align="center">Made while learning. Corrections and PRs welcome. ⭐</div>
