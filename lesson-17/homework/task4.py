import numpy as np
import matplotlib.pyplot as plt

x_values = np.random.randint(0,11,100)
y_values = np.random.randint(0,11,100)

plt.scatter(x_values, y_values, c = y_values, marker = "H",cmap = "cool")

plt.title("Scatter plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.show()