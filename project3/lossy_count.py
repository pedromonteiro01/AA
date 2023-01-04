from utils import get_upper_letters

def lossy_count(letters, epsilon, sigma):
    # sigma -> the minimum number of times that a letter must appear in the data stream for it to be considered frequent
    # epsilon -> is the error bound, determines the width of the buckets
    #              smaller values means that the counters for each letter will be updated less frequently
    #               => the algorithm will be less accurate
    
    letter_counters = {} # save all letters and counters
    frequent_letters = {} # save only letters that are frequent, using sigma to verify

    for letter in letters:
        if letter not in letter_counters:
            letter_counters[letter] = 0 # initialize each letter counter
    
    # create buckets of width w
    w = int(1/epsilon)
    buckets = [letters[i:i+w] for i in range(1, len(letters)+1, w)]
    
    for bucket in buckets:
        # increment each letter counter in the bucket
        for letter in bucket:
            letter_counters[letter] += 1
        
        # decrement all counters by 1
        for letter in letter_counters:
            letter_counters[letter] -= 1

    for letter, value in letter_counters.items():
        if value >= sigma:
            frequent_letters[letter] = value
    
    return frequent_letters

# get letters from file
letters = get_upper_letters("pg69638.txt")

# get frequent letters with lossy count function
frequent_letters = lossy_count(letters, 0.001, 15)

k_values = [3, 5, 10]
for k in k_values:
    with open(f"lossy_count_results/lossy_count-{k}.txt", "w") as f:
        f.write(f"Most Frequent Letters with k = {k}\n\n")

        # sort dict by values (higher values first) and get k first letters
        sorted_letters = sorted(frequent_letters.items(), key=lambda x: x[1], reverse=True)[:k]

        for item in sorted_letters:
            f.write(f"{item[0]} - {item[1]}\n")