import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, high and low temeratures from file.
filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)

    # Take the first line of the file.
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:

        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        # Convert string into intergers so the matplotlib can read them.
        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# Plot the data.
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = "red")
plt.plot(dates, lows, c = "blue")

# Format plot.
plt.title("Daily high and low temperatures, 2014", fontsize = 24)
plt.xlabel(" ", fontsize = 16)

# Draw the dates diagonally to prevent them from overlapping
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)

plt.show()