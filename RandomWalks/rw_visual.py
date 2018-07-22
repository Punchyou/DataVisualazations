import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks.
while True:
    # Make a random walk and plot the points.
    # Increase the number points.
    rw = RandomWalk(1000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi = 128, figsize = (10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.RdPu, edgecolor = "none", s = 10)
    
    # Emphasize the first and last points.
    plt.scatter(0, 0, c = "green", edgecolors = "none", s = 20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = "red", edgecolors = "none", s = 20)
    
    # Remove axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.title("Random Walks with first (green) and last (red) point indicated.", fontsize = 10)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break