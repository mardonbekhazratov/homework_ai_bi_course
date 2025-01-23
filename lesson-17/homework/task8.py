import numpy as np
import matplotlib.pyplot as plt

# Define the time periods and categories
time_periods = ['T1', 'T2', 'T3', 'T4']
categories = ['Category A', 'Category B', 'Category C']

# Sample data (each row corresponds to a category, each column to a time period)
data = np.array([
    [15, 20, 35, 40],  # Category A
    [25, 30, 15, 25],  # Category B
    [30, 10, 25, 20]   # Category C
])

# Bar width
bar_width = 0.6

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the stacked bar chart
bottom = np.zeros(len(time_periods))  # Track the bottom position of bars
colors = ['red', 'green', 'blue']  # Custom colors for each category

for i, category in enumerate(categories):
    ax.bar(time_periods, data[i], bottom=bottom, label=category, color=colors[i])
    bottom += data[i]  # Update the bottom position for stacking

# Customize the chart
ax.set_xlabel('Time Periods')
ax.set_ylabel('Value')
ax.set_title('Stacked Bar Chart of Categories Over Time')
ax.legend(title='Categories')

# Show the plot
plt.show()