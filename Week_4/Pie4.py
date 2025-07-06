import matplotlib.pyplot as plt
import numpy as np

# Data for the plots
pie_data = [30, 20, 50]
pie_labels = ['Category A', 'Category B', 'Category C']

line_x = np.array([1, 2, 3, 4, 5])
line_y = np.array([2, 5, 3, 6, 4])

bar_categories = ['Item X', 'Item Y', 'Item Z']
bar_values = [15, 25, 10]

# Create a figure and a set of subplots
# The (1, 3) argument creates a 1 row, 3 column grid of subplots
# figsize sets the size of the entire figure
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Plot the pie chart on the first axis (ax1)
ax1.pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=90)
ax1.set_title('Pie Chart')
ax1.axis('equal') # Ensures the pie chart is circular

# Plot the line graph on the second axis (ax2)
ax2.plot(line_x, line_y, marker='o', linestyle='-', color='blue')
ax2.set_title('Line Graph')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.grid(True)

# Plot the bar graph on the third axis (ax3)
ax3.bar(bar_categories, bar_values, color=['red', 'green', 'purple'])
ax3.set_title('Bar Graph')
ax3.set_xlabel('Categories')
ax3.set_ylabel('Values')

# Adjust layout to prevent overlapping titles/labels
plt.tight_layout()

# Display the plot
plt.show()