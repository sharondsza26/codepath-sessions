# Problem 8: Find the Difference of Two Signal Arrays
# You are given two 0-indexed integer arrays signals1 and signals2, representing signal data from two different probes. Return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in signals1 which are not present in signals2.
# answer[1] is a list of all distinct integers in signals2 which are not present in signals1.
# Note that the integers in the lists may be returned in any order.

# Below is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.

# 1. Convert signals1 and signals2 to sets.
# 2. Find the difference between set1 and set2 and store it in diff1.
# 3. Find the difference between set2 and set1 and store it in diff2.
# 4. Return the list [diff1, diff2].

def find_difference(signals1, signals2):
    s1 = set(signals1)
    s2 = set(signals2)
    
    return [list(s1 - s2) , list(s2 - s1)]

signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

signals1_example2 = [1, 2, 3, 3]
signals2_example2 = [1, 1, 2, 2]

print(find_difference(signals1_example1, signals2_example1)) 
print(find_difference(signals1_example2, signals2_example2))