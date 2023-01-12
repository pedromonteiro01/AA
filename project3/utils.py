import string
import matplotlib.pyplot as plt
import numpy as np

def get_upper_letters(file):
  # open the text file
  with open(file, 'r') as f:
    text = f.read()

  words = text.split()
  letters = []

  for word in words:
    for char in word: # iterate all chars
      if char not in string.punctuation and char.isalpha(): # check if char is not a punctuation mark
        letters.append(char.upper())

  # return list of all letters
  return letters

def show_bar_chart():
  x_axis = ['E', 'T', 'A', 'O', 'H']
  y_axis = [19470, 14301, 12178, 12034, 10383]
  #y_axis = [78117, 56723, 48695, 48478, 41920]

  plt.bar(x_axis, y_axis)
  plt.title('Top 5 Frequent Letters with Approximate Counter')
  plt.xlabel('Letters')
  plt.ylabel('Counters')
  plt.ylim(0, 90000)

  for x, y in zip(x_axis, y_axis):
      plt.text(x, y, y, ha='center', va='bottom')

  plt.show()

show_bar_chart()

def show_stacked_bar_chart():
  labels = ['E', 'T', 'O']
  exact_counter = [78117, 56723, 48695]
  lossy_count = [77504, 56110, 48082]

  x = np.arange(len(labels))  # the label locations
  width = 0.35  # the width of the bars

  fig, ax = plt.subplots()
  rects1 = ax.bar(x - width/2, exact_counter, width, label='Exact Counter')
  rects2 = ax.bar(x + width/2, lossy_count, width, label='Lossy Count')

  yticks = np.arange(40000, 91000, 10000)

  # Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_ylabel('Counters')
  ax.set_ylabel('Letters')
  ax.set_title('Top 3 Frequent Letters for Exact Counter and Lossy Count')
  ax.set_ylim(ymin=40000)
  ax.set_xticks(x, labels)
  ax.set_yticks(yticks)
  ax.legend()

  ax.bar_label(rects1, padding=3)
  ax.bar_label(rects2, padding=3)

  fig.tight_layout()

  plt.show()

def calculate_error():
  exact_letters = {
    "E" : 78117,
    "T" : 56723,
    "O" : 48695,
    "A" : 48478,
    "H" : 41920,
    "N" : 41451,
    "I" : 38731,
    "S" : 37375,
    "R" : 35616,
    "D" : 26803
  }

  letters = {
    "E" : 77504,
    "T" : 56110,
    "A" : 48082,
    "O" : 47865,
    "H" : 41307,
    "N" : 40838,
    "I" : 38118,
    "S" : 36762,
    "R" : 35003,
    "D": 26190,
  }

  total_items = 78117
  avg_error = 0
  for k,v in letters:
    for k1,v1 in exact_letters:
      error = 

#show_stacked_bar_chart()