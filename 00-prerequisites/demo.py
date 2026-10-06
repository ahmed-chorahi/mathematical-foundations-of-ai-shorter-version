import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 200)
fig, ax = plt.subplots(1, 3, figsize=(10, 3))
ax[0].plot(x, 2*x + 1); ax[0].set_title("f(x)=2x+1")
ax[1].plot(x, np.exp(x)); ax[1].set_title("e^x")
xp = np.linspace(0.05, 5, 200)
ax[2].plot(xp, np.log(xp)); ax[2].set_title("ln(x)")
for a in ax: a.grid(alpha=.3)
plt.tight_layout(); plt.savefig("functions.png", dpi=100)
print("log(0.5^3) =", np.log(0.5**3), "| 3*log(0.5) =", 3*np.log(0.5))
print("distance (3,4):", np.sqrt(3**2 + 4**2))
