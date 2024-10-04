import numpy as np
import matplotlib.pyplot as plt

# Generate random walk
n_steps = 1000
x = np.cumsum(np.random.randn(n_steps))
y = np.cumsum(np.random.randn(n_steps))

plt.plot(x, y, label="Random Walk")
plt.title("2D Random Walk")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
