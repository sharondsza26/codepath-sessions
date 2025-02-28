# Problem 9: Common Signals Between Space Probes
# Two space probes have collected signals represented by integer arrays signals1 and signals2 of sizes n and m, respectively. Calculate the following values:

# answer1: the number of indices i such that signals1[i] exists in signals2.
# answer2: the number of indices j such that signals2[j] exists in signals1.
# Return [answer1, answer2].

def find_common_signals(signals1, signals2):
    s1 = set(signals1)
    s2 = set(signals2)
    count1 = 0
    count2 = 0
    
    for i in signals1:
        if i in s2:
            count1 += 1
            
    for i in signals2:
        if i in s1:
            count2 += 1
            
    return [count1 , count2]

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))