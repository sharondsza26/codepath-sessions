# Problem 2: Booking the Perfect Cruise Cabin
# As part of your cruise planning, you have a list of available cabins sorted in ascending order by their deck level. Given the list of available cabins represented by deck level, cabins, and an integer preferred_deck, write a recursive function find_cabin_index() that returns the index of preferred_deck. If a cabin with your preferred_deck does not exist in cabins, return the index where it would be if it were added to the list to maintain the sorted order.

# Your algorithm must have O(log n) time complexity.

def find_cabin_index(cabins, preferred_deck):
    def helper(left, right):
        if left > right:
            return left
        
        mid = (left+right) //2 
        
        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] < preferred_deck:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)
        
    return helper(0, len(cabins) - 1)
# Example Usage:

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))
# Example Output:

# 2
# 1
# 4
