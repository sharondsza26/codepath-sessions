# Problem 7: Good Things Come in Threes
# Write a function make_divisible_by_3() that accepts an integer array nums. In one operation, 
# you can add or subtract 1 from any element of nums. 
# Return the minimum number of operations to make all elements of nums divisible by 3.

def make_divisible_by_3(nums):
    count_mod1 = 0  # Count of numbers with remainder 1 when divided by 3
    count_mod2 = 0  # Count of numbers with remainder 2 when divided by 3
    
    # Count numbers that are not divisible by 3
    for num in nums:
        if num % 3 == 1:
            count_mod1 += 1
        elif num % 3 == 2:
            count_mod2 += 1
    
    return count_mod1 + count_mod2

nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))