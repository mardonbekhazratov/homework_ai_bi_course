import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 2 * np.pi, 50)
sinx_values = np.sin(x_values)
cosx_values = np.cos(x_values)

plt.figure(figsize=(8, 6))

plt.plot(x_values, sinx_values, linestyle = ":", marker = "o", color = "green", label = r"$\sin(x)$")
plt.plot(x_values, cosx_values, linestyle = "-.", marker = "<", color = "red", label = r"$\cos(x)$")

plt.title('Plot of $ \sin(x) $ and $ \cos(x) $')
plt.xlabel("x")
plt.legend()

plt.show()