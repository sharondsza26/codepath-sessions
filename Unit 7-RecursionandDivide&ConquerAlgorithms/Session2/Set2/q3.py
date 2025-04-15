# Problem 3: Sqrt(x)
# Given a non-negative integer x, use binary search to return the square root of x 
# rounded down to the nearest integer. The returned integer should be non-negative as well.

# You may not use any built-in exponent function or operator. You may not use any external 
# libraries like math.

# For example, do not use pow(x, 0.5) or x ** 0.5.
# Evaluate the time and space complexity of your solution. Define your variables and 
# provide a rationale for why you believe your solution has the stated time and space complexity.

def my_sqrt(x):
    def helper(left, right):
        if left > right:
            return right  # right is the floor of sqrt(x)

        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)

    if x < 2:
        return x
    return helper(1, x // 2)
# Example Usage:

print(my_sqrt(4))
print(my_sqrt(8))
# Example Output:

# 2
# 4
# Example 2 Explanation: The square root of 8 is 2.82842..., and since we round it down 
# to the nearest integer, the answer is 2. 
