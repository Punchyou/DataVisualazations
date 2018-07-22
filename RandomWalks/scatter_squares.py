import matplotlib.pyplot as plt

x_values = list(range(1, 16))
y_values = [x**2 for x in x_values]

# Using a blues color map.
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = "black", s = 70)

#Title and label titles.
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 15)
plt.ylabel("Squared Values", fontsize = 15)

# Set size of tick labels.
plt.tick_params(axis = "both", labelsize = 12)

# Set range for each axis.
plt.axis([0, 15.5, -4, 230])
plt.show()

# Save the plot
#plt.savefig("squares_plot.png", )