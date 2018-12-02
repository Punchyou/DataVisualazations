import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, high and low temeratures from file.
filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)

    # Take the first line of the file.
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:

            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        
        else:

            # Convert string into intergers so the matplotlib can read them.
            dates.append(current_date)
            highs.append(high)    
            lows.append(low)

# Plot the data.
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = "red", alpha = 0.5) # alpha for transparency
plt.plot(dates, lows, c = "blue", alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = "purple", alpha = 0.3)

# Format plot.
plt.title("Daily high and low temperatures, Death Valley", fontsize = 24)
plt.xlabel(" ", fontsize = 16)

# Draw the dates diagonally to prevent them from overlapping
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)

plt.show()