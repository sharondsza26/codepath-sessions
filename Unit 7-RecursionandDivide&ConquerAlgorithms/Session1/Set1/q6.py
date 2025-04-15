# Problem 6: Strongest Avenger
# The Avengers need to determine who is the strongest. Given a list of their strengths, 
# find the maximum strength using a recursive approach without using the max() function.

# Evaluate the time complexity of your solution. Define your variables and provide a rationale 
# for why you believe your solution has the stated time complexity.

def strongest_avenger(strengths):
    if 1 == len(strengths):
        return 0
        
    max = strongest_avenger(strengths[1:])
    return strengths[0] if strengths[0] > max else max
# Example Usage:

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))
# Example Output:

# 100
# Example 1 Explanation: The maximum strength among the Avengers is 100.

# 90
# Example 2 Explanation: The maximum strength among the Avengers is 90.