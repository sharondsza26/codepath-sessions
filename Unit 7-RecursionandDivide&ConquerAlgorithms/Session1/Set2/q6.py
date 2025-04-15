# Problem 6: Checking the Knight's Path
# A knight is traveling along a path marked by stones, and each stone has a number on it. The knight must check if the numbers on the stones form a strictly increasing sequence. Write a recursive function to determine if the sequence is strictly increasing.

# Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def is_increasing_path(path):
    if len(path) <= 1:
        return True
    if path[0] < path[1]:
        return is_increasing_path(path[1:])
    
    return False

# Example Usage:

print(is_increasing_path([1, 2, 3, 4, 5]))
print(is_increasing_path([3, 5, 2, 8]))
# Example Output

# True
# False