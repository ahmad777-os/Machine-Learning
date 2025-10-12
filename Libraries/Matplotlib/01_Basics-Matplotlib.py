import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)

plt.plot(x, y)  # Line plot
plt.title("Sine Wave")  # Title
plt.xlabel("X-axis (Time)")  # Label x-axis
plt.ylabel("Y-axis (Amplitude)")  # Label y-axis
plt.grid(True)  # Show grid
plt.show()


# plt.plot() → basic line plot

# plt.scatter() → scatter plot (great for datasets)

# plt.bar() → bar chart

# plt.hist() → histogram (great for distributions)

