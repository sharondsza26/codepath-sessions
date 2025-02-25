# Problem 6: Smaller Than
# Write a function smaller_than_current that accepts a list of integers nums and, 
# for each element in the list nums[i], determines the number of other elements 
# in the array that are smaller than it. More formally, for each nums[i] count the number of 
# valid j's such that j != i and nums[j] < nums[i].

# Return the answer as a list.

def smaller_than_current(nums):
    smaller = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i == j:
                continue
            
            if nums[j] < nums[i]:
                count += 1
                
        smaller.append(count)
        
    print(smaller)

nums = [8, 1, 2, 2, 3]
smaller_than_current(nums)

nums = [6, 5, 4, 8]
smaller_than_current(nums)

nums = [7, 7, 7, 7]
smaller_than_current(nums)