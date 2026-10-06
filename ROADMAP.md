# 🗺️ Roadmap

```text
Basic Math → Linear Algebra → Calculus → Probability → Statistics → Optimization
          → Information Theory → ML → Neural Networks → Transformers → LLMs
```

| # | Stage | You learn | You can now understand |
|---|---|---|---|
| 00 | [Prerequisites](00-prerequisites/) | algebra, functions, exp/log, Σ, geometry, notation | formulas in ML papers |
| 01 | [Linear Algebra](01-linear-algebra/) | vectors, matrices, dot product, norms, eigen, PCA, SVD | how data and layers are represented |
| 02 | [Calculus](02-calculus/) | derivatives, partials, chain rule, gradient, Jacobian, Hessian | how a loss can be reduced |
| 03 | [Probability](03-probability/) | random variables, Bayes, expectation, distributions | models that output probabilities |
| 04 | [Statistics](04-statistics/) | variance, correlation, confidence, p-values | honest evaluation |
| 05 | [Optimization](05-optimization/) | gradient descent, SGD, momentum, Adam | how training actually moves weights |
| 06 | [Information Theory](06-information-theory/) | entropy, cross-entropy, KL, MI | why cross-entropy is *the* loss |
| 07 | [ML Math](07-machine-learning-math/) | regression, softmax, MLE, regularization, bias-variance | classic ML end to end |
| 08 | [Neural Network Math](08-neural-network-math/) | neurons, activations, backprop, training loop | deep learning from scratch |
| 09 | [Transformer Math](09-transformer-math/) | embeddings, Q/K/V, attention, LayerNorm | the architecture behind modern AI |
| 10 | [LLM Math](10-llm-math/) | next-token loss, perplexity, temperature, top-k/p | how LLMs train and generate |

## Suggested pace

| Week | Chapters |
|---|---|
| 1 | 00, 01 |
| 2 | 02, 03 |
| 3 | 04, 05 |
| 4 | 06, 07 |
| 5 | 08 |
| 6 | 09, 10 |

## Dependencies (what to read first)

```text
00 ─► 01 ─► 02 ─► 05 ─► 08 ─► 09 ─► 10
 └──► 03 ─► 04 ──┘      ▲      ▲
       └──► 06 ─► 07 ───┘──────┘
```

## Where to go after this

- Build a small neural network library from scratch.
- Implement a mini-GPT (character level) with NumPy, then PyTorch.
- Read *Attention Is All You Need* and follow every formula with the notation from chapter 00.
