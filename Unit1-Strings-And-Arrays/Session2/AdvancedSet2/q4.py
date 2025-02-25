# Problem 4: Two-Pointer Two Sum
# Use the two pointer approach to implement a function two_sum() that takes in a 
# sorted list of integers nums and an integer target as parameters and returns the indices of 
# the two numbers that add up to target. You may assume that each input would have exactly one solution,
# and you may not use the same element twice. You can return the indices in any order.

def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            print([left, right])
            
        if sum > target:
            right -= 1
            
        else: 
            left += 1 
        

nums = [2, 7, 11, 15]
target = 9
two_sum(nums, target)

nums = [2, 7, 11, 15]
target = 18
two_sum(nums, target)
