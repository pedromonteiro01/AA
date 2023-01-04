from utils import get_upper_letters

def lossy_count(letters, epsilon, sigma):
    # sigma -> the minimum number of times that a letter must appear in the data stream for it to be considered frequent
    # epsilon -> is the error bound, determines the width of the buckets
    #              smaller values means that the counters for each letter will be updated less frequently
    #               => the algorithm will be less accurate
    
    counters = {}

    # initialize counters for each letter
    for letter in letters:
        if letter not in counters:
            counters[letter] = 0
    
    # create buckets of width w
    w = int(1/epsilon)
    buckets = [letters[i:i+w] for i in range(1, len(letters)+1, w)]
    
    for bucket in buckets:
        # increment counters for each letter in the bucket
        for letter in bucket:
            counters[letter] += 1
        
        # decrement all counters by 1
        for letter in counters:
            counters[letter] -= 1
    
    # return frequent letters
    frequent_letters = {}
    for letter, count in counters.items():
        if count >= sigma:
            frequent_letters[letter] = count
    
    return frequent_letters

# get letters from file
letters = get_upper_letters("pg69638.txt")

frequent_letters = lossy_count(letters, 0.001, 15)

k_values = [3, 5, 10]
for k in k_values:
    with open(f"lossy_count_results/lossy_count-{k}.txt", "w") as f:
        f.write(f"Most Frequent Letters with k = {k}\n\n")

        # sort dict by values (higher values first) and get k first letters
        sorted_letters = sorted(frequent_letters.items(), key=lambda x: x[1], reverse=True)[:k]

        for item in sorted_letters:
            f.write(f"{item[0]} - {item[1]}\n")