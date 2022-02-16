import matplotlib.pyplot as plt
from typing import NamedTuple
import csv

# setting structure
class DUST(NamedTuple):
  LOW_DUST : list
  HIGEST_DUST : list
  AVERAGE_DUST : list
  line_color : list
  line_style : list
  width : int
  height : int
  month_term : int

# setting variable
dust = DUST(HIGEST_DUST=list(),
            LOW_DUST=list(),
            AVERAGE_DUST=list(), 
            width=50, # window width
            height=8, # window height
            month_term = 475,
            # select your line color
            line_color = ["b", # blue 0
                          "g", # green 1
                          "r", # red 2
                          "c", # sky blue 3
                          "m", # purple 4
                          "y", # yellow 5
                          "k"], # black 6
            # select your line style
            line_style = ["^", # 0
                          "v", # 1
                          ">", # 2
                          "<", # 3
                          "o", # 4
                          "*", # 6
                          "+", # 7
                          "1", # 8
                          "2", # 9
                          "3"])# 10

def get_file(list, index):
  f = open("pouder2.csv", "r", encoding="utf-8") # get data from .csv file
  data = csv.reader(f)
  next(data) # skip first line
  for row in data:
    list.append(float(row[int(index)]))

def show():
  plt.figure(figsize=(dust.width, dust.height)) # setting window's width, height
  plt.plot(dust.HIGEST_DUST, "%s%s" % (dust.line_color[2], dust.line_style[-3]), label="HIGHEST DUST") # HIGHEST_DUST
  plt.plot(dust.LOW_DUST, "%s%s" % (dust.line_color[3],dust.line_style[-2]), label="LOW DUST") # LOW_DUST
  plt.plot(dust.AVERAGE_DUST, "%s%s" % (dust.line_color[1],dust.line_style[-1]), label="AVERAGE DUST") # AVERAGE_DUST
  plt.plot("k-", label="MONTH") # Month
  for i in range(12):
    plt.plot([dust.month_term * i, dust.month_term * i], [-200, 1300], "k-") # Month
  plt.legend()
  plt.title("Dust rate Graph 2020-10-01 to 2021-08-04") # show the graph title
  plt.ylabel("Dust rate")
  plt.xlabel("time(day)")
  plt.savefig("Dust.png") # download .png file
  plt.show()

if __name__ == "__main__":
  get_file(dust.HIGEST_DUST, 6)
  get_file(dust.LOW_DUST, 8)
  get_file(dust.AVERAGE_DUST, 2)
  show()