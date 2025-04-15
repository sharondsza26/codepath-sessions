# Problem 3: Count Checked In Passengers
# As a cruise ship worker, you're in charge of tracking how many passengers have checked in to their rooms thus far. You are given a list of rooms where passengers are either checked in (represented by a 1) or not checked in (represented by a 0). The list is sorted, so all the 0s appear before any 1s.

# Write a function count_checked_in_passengers() that efficiently counts and returns the total number of checked-in passengers (1s) in the list in O(log n) time.

def count_checked_in_passengers(rooms):
    def binary_search(left, right):
        if left > right:
            return len(rooms)  
        
        mid = (left + right) // 2
        
        if rooms[mid] == 1:
            
            if mid == 0 or rooms[mid - 1] == 0:
                return mid
            else:
                return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)

    first_one_index = binary_search(0, len(rooms) - 1)
    return len(rooms) - first_one_index
# Example Usage:

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))
# Example Output:

# 4
# 1
# 0