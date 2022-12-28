from utils import get_upper_letters

# get letters from file
letters = get_upper_letters("pg69638.txt")

# dictionary to store letter counts
letter_counts = {}

# iterate all letters
for letter in letters:
    if letter in letter_counts: # if letters is already in dict, just count +1
        letter_counts[letter] += 1
    else: # else initialize a counter to a new letter
        letter_counts[letter] = 1

k_values = [3, 5, 10]
for k in k_values:
    with open(f"exact_counter_results/exact_counter-{k}.txt", "w") as f:
        f.write(f"Most Frequent Letters with k = {k}\n\n")

        # sort dict by values (higher values first) and get k first letters
        sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)[:k]

        for item in sorted_letters:
            f.write(f"{item[0]} - {item[1]}\n")