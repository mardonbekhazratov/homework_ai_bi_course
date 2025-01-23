import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = ["red", "green", "blue", "yellow", "cyan"]

plt.bar(products, values, color = colors, width = 0.5)
plt.title("Sales data for five different products")
plt.xlabel("Products")
plt.ylabel("Sales values")

plt.show()