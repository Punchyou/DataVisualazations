import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 3)

#Title and label titles.
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 15)
plt.ylabel("Squared Values", fontsize = 15)

# Set size of tick labels.
plt.tick_params(axis = "both", labelsize = 12)

plt.show()