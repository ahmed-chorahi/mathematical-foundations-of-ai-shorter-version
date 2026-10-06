# Local vs Global Minima

*📓 Notes · [05 · Optimization](../README.md) · what to minimize*

**📝 In simple words:** A local minimum is the lowest point nearby; the global one is the lowest overall.

```text
 loss
  │ \      /\
  │  \    /  \      /
  │   \__/    \____/
  │    ↑local    ↑global
  └──────────────────► w
```

**🤖 Why AI uses it:** in very high dimensions most trouble comes from saddle points and flat regions, not bad local minima. Convex losses (like linear regression's) have only one minimum.

**🧪 Try it myself:** How many minima does `x²` have? <details><summary>Solution</summary>One, the global minimum at 0.</details>

---
← [Objective & Loss Functions](../1-what-to-minimize/01-objective-loss-functions.md)  |  [Gradient Descent](../2-gradient-descent-family/03-gradient-descent.md) →
