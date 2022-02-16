import matplotlib.pyplot as plt
import numpy as np
import csv

r = 0.1
theta = np.deg2rad(60.0)

fig = plt.figure()

ax = fig.add_subplot(111, projection='polar')
f = open("wind_direction.csv", "r") # get data from .csv file
data = csv.reader(f)
next(data)
li = list()
for row in data:
    ax.scatter(row[1],r)
    r+=0.05

ax.set_xticks(np.arange(0,2.0*np.pi,np.pi/6.0))
ax.set_ylim(0,30)
ax.set_yticks(np.arange(0,50,1.0))

plt.show()