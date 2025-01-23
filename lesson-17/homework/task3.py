import numpy as np
import matplotlib.pyplot as plt

# Define x values for each function
x1 = np.linspace(-2, 2, 100)  # For x^3
x2 = np.linspace(-np.pi, np.pi, 100)  # For sin(x)
x3 = np.linspace(-2, 2, 100)  # For e^x
x4 = np.linspace(0, 5, 100)  # For log(x+1)

# Compute function values
y1 = x1**3
y2 = np.sin(x2)
y3 = np.exp(x3)
y4 = np.log(x4 + 1)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

print(axs)
# Top-left: f(x) = x^3
axs[0, 0].plot(x1, y1, color='blue')
axs[0, 0].set_title(r'$ f(x) = x^3 $')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')

# Top-right: f(x) = sin(x)
axs[0, 1].plot(x2, y2, color='red')
axs[0, 1].set_title(r'$ f(x) = \sin(x) $')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')

# Bottom-left: f(x) = e^x
axs[1, 0].plot(x3, y3, color='green')
axs[1, 0].set_title(r'$ f(x) = e^x $')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')

# Bottom-right: f(x) = log(x+1)
axs[1, 1].plot(x4, y4, color='purple')
axs[1, 1].set_title(r'$ f(x) = \log(x+1) $')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()