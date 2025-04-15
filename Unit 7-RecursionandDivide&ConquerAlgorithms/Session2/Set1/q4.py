# Problem 4: Determining Profitability of Excursions
# As the activities director on a cruise ship, you’re organizing excursions for the passengers. You have a sorted list of non-negative integers excursion_counts, where each number represents the number of passengers who have signed up for various excursions at your next cruise destination. The list is considered profitable if there exists a number x such that there are exactly x excursions that have at least x passengers signed up.

# Write a function that detrmines whether excursion_counts is profitable. If it is profitable, return the value of x. If it is not profitable, return -1. It can be proven that if excursion_counts is profitable, the value for x is unique.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


def is_profitable(excursion_counts):
    n = len(excursion_counts)
    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2

        
        lo, hi = 0, n - 1
        index = n
        while lo <= hi:
            m = (lo + hi) // 2
            if excursion_counts[m] >= mid:
                index = m
                hi = m - 1
            else:
                lo = m + 1

        count = n - index

        if count == mid:
            return mid
        elif count > mid:
            left = mid + 1
        else:
            right = mid - 1

    return -1
# Example Usage:

print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
# Example Output:

# 2
# Example 1 Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

# -1 
# Example 2 Explanation: No numbers fit the criteria for x.
#     - If x = 0, there should be 0 numbers >= x, but there are 2.
# 	- If x = 1, there should be 1 number >= x, but there are 0.
# 	- If x = 2, there should be 2 numbers >= x, but there are 0.
# 	- x cannot be greater since there are only 2 numbers in nums.