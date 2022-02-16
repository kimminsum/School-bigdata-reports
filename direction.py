import matplotlib.pyplot as plt
import csv

f = open("wind_direction.csv", "r", encoding="utf-8") # get data from .csv file
data = csv.reader(f)
next(data)
direction = list()
for row in data:
    if 0 <= float(row[1]) <= 30 or 330 <= float(row[1]) <= 360: # north
        direction.append("N")
    elif 60 <= float(row[1]) <= 120: # east
        direction.append("E")
    elif 150 <= float(row[1]) <= 210: # south
        direction.append("S")
    elif 240 <= float(row[1]) <= 300: # west
        direction.append("W")
plt.figure(figsize=(50, 8))
plt.plot(direction,"r+")
plt.title("Wind direction Graph")
plt.ylabel("wind direction")
plt.xlabel("time(hour)")
plt.savefig("wind_direction.png") # download .png file
plt.show()