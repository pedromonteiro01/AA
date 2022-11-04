import matplotlib.pyplot as plt
from utils import show_results_graph
import os

exhaustive_x_12 = []
exhaustive_x_25 = []
exhaustive_x_50 = []
exhaustive_x_75 = []
exhaustive_y = [4,5,7,8,9,11,12,13]

file = 'brute_force_results.txt'
if os.path.exists(file):
    with open(file) as f:
        f.readline()
        for line in f:
            data = line.split()
            if str(data[1]) == "12.5":
                exhaustive_x_12.append(data[4])
            if str(data[1]) == "25":
                exhaustive_x_25.append(data[4])
            if str(data[1]) == "50":
                exhaustive_x_50.append(data[5])
            if str(data[1]) == "75":
                exhaustive_x_75.append(data[4])
f.close()

print(exhaustive_x_12)
print(exhaustive_x_25)
for e in exhaustive_x_50:
    print(e)
print(exhaustive_x_75)
print(exhaustive_y)
print(len(exhaustive_x_12))
print(len(exhaustive_x_25))
print(len(exhaustive_x_50))
print(len(exhaustive_x_75))
print(len(exhaustive_y))

plt.plot(exhaustive_x_50, exhaustive_y)
plt.ylim([2,20])
plt.yscale('log')
plt.show()
