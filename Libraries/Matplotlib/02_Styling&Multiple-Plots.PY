import matplotlib.pyplot as plt
import numpy as np
# Multiple plots
x = np.linspace(0, 5, 50)
plt.plot(x, x, label='y = x', color='r', linestyle='--')
plt.plot(x, x**2, label='y = x^2', color='b')
plt.plot(x, np.sqrt(x), label='y = √x', color='g')

plt.legend()  # Show labels
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
# Subplots (multiple plots in one figure):
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, np.sin(x), color='m')
axes[0].set_title('Sine')

axes[1].plot(x, np.cos(x), color='c')
axes[1].set_title('Cosine')

plt.show()
