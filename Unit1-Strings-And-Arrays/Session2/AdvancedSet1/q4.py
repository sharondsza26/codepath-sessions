# Problem 4: Sort Array by Parity
# Given an integer array nums, write a function sort_by_parity() 
# that moves all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

def sort_by_parity(nums):
    left = 0  # Pointer for even numbers
    
    for right in range(len(nums)):
        if nums[right] % 2 == 0:  # If even
            nums[left], nums[right] = nums[right], nums[left]  # Swap
            left += 1  # Move even pointer forward
    
    print(nums)
    return nums
            


nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)