# Problem 8: Left and Right Sum Differences
# Given a 0-indexed integer array nums, write a function left_right_difference that 
# returns a 0-indexed integer array answer where:

# len(answer) == len(nums)
# answer[i] = left_sum[i] - right_sum[i]
# Where:

# left_sum[i] is the sum of elements to the left of the index i in the array nums. 
# If there is no such element, left_sum[i] = 0
# right_sum[i] is the sum of elements to the right of the index i in the array nums. 
# If there is no such element, right_sum[i] = 0

def left_right_difference(nums):
    answer = []
    left_sum = 0
    right_sum = sum(nums)
    
    for i in range(len(nums)):
        right_sum -= nums[i]
        current_element = left_sum - right_sum
        left_sum += nums[i]
        answer.append(current_element)
        
    print(answer)
    

nums = [10, 4, 8, 3]
left_right_difference(nums)

nums = [1]
left_right_difference(nums)