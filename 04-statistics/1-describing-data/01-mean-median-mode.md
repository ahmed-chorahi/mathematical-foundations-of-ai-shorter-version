# Mean, Median, Mode

*📓 Notes · [04 · Statistics](../README.md) · describing data*

**📝 In simple words:** Three ways to describe the "center" of data.

**🔢 Small example:** `[2, 4, 4, 6, 9]`

**📐 Formula to remember:** mean `= Σxᵢ/n`; median = middle value when sorted; mode = most frequent.

**✏️ Let me calculate it:** mean `25/5 = 5`; median `4`; mode `4`. One outlier (say 90) would drag the mean to 17.7 but leave the median at 4.

**🤖 Why AI uses it:** the mean is the basis of the loss average and normalization; the median resists outliers (MAE vs MSE, chapter 07).

```python
import numpy as np
from collections import Counter
d = [2, 4, 4, 6, 9]
print(np.mean(d), np.median(d), Counter(d).most_common(1)[0][0])
```

**🧪 Try it myself:** Mean and median of `[1, 2, 3, 100]`? <details><summary>Solution</summary>Mean 26.5, median 2.5.</details>

---
[Variance & Standard Deviation](../1-describing-data/02-variance-standard-deviation.md) →
