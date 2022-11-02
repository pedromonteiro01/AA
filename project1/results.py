import matplotlib.pyplot as plt
from utils import show_results_graph
import os

time2 = []
edges = []
time = []
dic = {}

file = 'brute_force_results.txt'
if os.path.exists(file):
    with open(file) as f:
        f.readline()
        for line in f:
            data = line.split()
            edges.append(data[0])
            time.append(data[4])
f.close()
for e in edges:
    print(e)
input()
for t in time:
    print(t)
input()
file = 'brute_force_results.txt'
if os.path.exists(file):
    with open(file) as f:
        f.readline()
        for line in f:
            data = line.split()
            dic[data[0]] = data[4]

greedy_y = []
greedy_x = []
exhaustive_y = []
exhaustive_x = []

plt.plot(exhaustive_x, exhaustive_y)
plt.plot(greedy_x, greedy_y)
plt.yscale('symlog')
plt.show()
