from utils import get_upper_letters

# get letters
letters = get_upper_letters("pg69638.txt")
print(letters)

# create a dictionary to store the letter counts
letter_counts = {}

for letter in letters:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

k_values = [3, 5, 10]
for k in k_values:
    with open(f"exact_counter_results/exact_counter-{k}.txt", "w") as f:
        f.write(f"Most Frequent Letters with k = {k}\n\n")
        sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)[:k]

        for item in sorted_letters:
            f.write(f"{item[0]} - {item[1]}\n")