import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

f = lambda x: x**2 - 4*x + 5
x = np.linspace(-1, 5, 200)
plt.plot(x, f(x), label="f(x)")
for x0 in (0, 2, 4):
    slope = 2*x0 - 4
    t = np.linspace(x0-1, x0+1, 10)
    plt.plot(t, f(x0) + slope*(t-x0), "--", label=f"slope {slope} at x={x0}")
plt.legend(); plt.grid(alpha=.3); plt.savefig("derivative.png", dpi=100)
print("minimum at x = 2, f = 1")
