# Problem 9: Odd
# Write a function get_odds() that takes in a list of integers nums and 
# returns a new list containing all the odd numbers in nums.

def get_odds(nums):
    odd = []
    for i in nums:
        if i % 2 != 0:
            odd.append(i)
            
    print(odd)
    

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)