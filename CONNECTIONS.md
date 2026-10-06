# 🕸️ Concept Connections

## The main chain

```text
Vectors
   ↓
Matrices
   ↓
Linear Regression
   ↓
Neural Networks
   ↓
Embeddings
   ↓
Attention
   ↓
Transformers
   ↓
LLMs
```

## What feeds what

```text
 Algebra ─► Functions ─► Derivatives ─► Gradients ─► Gradient Descent ─┐
                              │                                         ▼
 Vectors ─► Dot product ─► Matrices ─► Linear layers ─► Backprop ─► Neural Networks
    │            │                                                      │
    │            └───────────────► Attention scores (QKᵀ)             │
    ▼                                                                   ▼
 Embeddings ──────────────────────────────► Attention ─► Transformers ─► LLMs
                                                               ▲
 Probability ─► Conditional prob ─► Language model P(next|past)┤
      │                                                        │
      └─► Entropy ─► Cross-entropy ─► Training loss ───────────┘
```

## Concept → where it reappears

| Concept (chapter) | Shows up later as |
|---|---|
| Dot product (01) | neuron weighted sum (08), attention score (09), cosine similarity (10) |
| Matrix multiply (01) | every layer `Wx+b` (08), `QKᵀ`, FFN (09) |
| Eigenvectors (01) | PCA (01, 07) |
| SVD / rank (01) | low-rank approximations, LoRA |
| Chain rule (02) | backpropagation (08) |
| Gradient (02) | gradient descent, Adam (05) |
| Exp & log (00) | softmax (07), log-likelihood (10) |
| Conditional probability (03) | next-token prediction (10) |
| Bayes (03) | priors, posteriors, Naive Bayes |
| Normal distribution (03) | weight init, noise model, MSE as MLE (07) |
| Variance (03/04) | normalization, LayerNorm (09), bias-variance (07) |
| Confidence intervals (04) | trustworthy evaluation |
| Gradient descent (05) | training loop (08) |
| Entropy / KL (06) | cross-entropy loss, RLHF penalty, distillation |
| MLE (07) | MSE, BCE, cross-entropy are all derived from it |
| Softmax (07) | attention weights (09), output probabilities (10) |
| Regularization (07) | weight decay in AdamW |
| Residual + LayerNorm (09) | stable deep Transformers |
| Perplexity (10) | `exp(cross-entropy)` |

## One loss, many names

```text
Maximum likelihood ─► minimize negative log-likelihood
                        ├─ Gaussian noise    → MSE
                        ├─ Bernoulli labels  → Binary cross-entropy
                        └─ Categorical/token → Cross-entropy ─► exp() ─► Perplexity
```

## One forward pass of an LLM, as math

```text
tokens ─► ids ─► E[ids] + PE ─► [ LayerNorm → Attention → +residual
                                  LayerNorm → FFN       → +residual ] × N
       ─► logits ─► softmax ─► P(next token) ─► sample (temperature / top-k / top-p)
```
