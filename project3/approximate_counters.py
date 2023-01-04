import random
from utils import get_upper_letters

# get letters from file
letters = get_upper_letters("pg69638.txt")

# dictionary to store letter counts
letter_counts = {}

for letter in letters:
    # increment counter with probability 1/4
    if random.random() < 1/4:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

k_values = [3, 5, 10]
for k in k_values:
    with open(f"approximate_counter_results/approximate_counter-{k}.txt", "w") as f:
        f.write(f"Most Frequent Letters with k = {k}\n\n")

        # sort dict by values (higher values first) and get k first letters
        sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)[:k]

        for item in sorted_letters:
            f.write(f"{item[0]} - {item[1]}\n")