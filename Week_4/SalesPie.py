import matplotlib.pyplot as plt

# Data for the pie chart
sizes = [350, 450, 300, 600]
labels = ['Product A', 'Product B', 'Product C', 'Product D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # "explode" the first slice (Product A)

# Plotting the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Add a title
plt.title('Sales Distribution by Product')

# Ensure the circle is drawn properly
plt.axis('equal')

# Display the chart
plt.show()