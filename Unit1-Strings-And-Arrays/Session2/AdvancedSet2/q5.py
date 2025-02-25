# Problem 5: Three Sum
# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def three_sum(nums):
    nums.sort()  # Sort the array to use the two-pointer technique
    res = []
    
    for i in range(len(nums) - 2):  
        if i > 0 and nums[i] == nums[i - 1]:  
            continue  # Skip duplicate elements for 'i'

        left, right = i + 1, len(nums) - 1  

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicates for 'left' and 'right'
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1  
            else:
                right -= 1  

    print(res)
    return res

nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)

nums = [0, 1, 1]
three_sum(nums)

nums = [0, 0, 0]
three_sum(nums)