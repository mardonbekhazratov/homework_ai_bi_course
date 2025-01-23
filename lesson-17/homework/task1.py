import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(-10,10,1000)
y_values = x_values ** 2 - 4 * x_values + 4

plt.plot(x_values, y_values, label = r'$f(x) = x^2 - 4x + 4$', color = "blue")
plt.title("Plot of the function $f(x) = x^2 - 4x + 4$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()