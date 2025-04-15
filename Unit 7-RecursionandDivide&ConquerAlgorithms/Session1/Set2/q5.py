# Problem 5: Doubling the Power of a Spell
# The court magician is practicing a spell that doubles its power with each incantation. 
# Given an integer initial_power and a non-negative integer n, write a recursive function 
# that doubles initial_power n times.

# Evaluate the time complexity of your solution. Define your variables and provide a 
# rationale for why you believe your solution has the stated time complexity.

def double_power(initial_power, n):
    if n == 0:
        return initial_power
    
    
    return double_power(2 * initial_power, n-1)
# Example Usage:

print(double_power(5, 3))
print(double_power(7, 2))

# Example Output

# 40
# Example 1 Explanation: 5 doubled 3 times: 5 -> 10 -> 20 -> 40

# Output: 28
# Example 2 Explanation: 7 doubled 2 times: 7 -> 14 -> 28