# Problem 5: Missing Clues
# Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day 
# and several hidden clues have blown away. Write a function find_missing_clues() 
# to help Christopher Robin figure out which clues he needs to remake. 
# The function accepts two integers lower and upper and a unique integer array clues. 
# All elements in clues are within the inclusive range [lower, upper].

# A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers.
# That is, no element of clues is included in any of the ranges, and each missing number 
# is covered by one of the ranges.

def find_missing_clues(clues, lower, upper):
    missing_ranges = []
    clues.sort()  # Ensure clues are sorted
    prev = lower - 1  # Start before the lower bound
    
    # Iterate over all given clues plus an extra number (upper + 1)
    for num in clues + [upper + 1]:
        if num - prev > 1:  # Check if there is a gap
            if num - prev == 2:  
                missing_ranges.append([prev + 1, prev + 1])  # Single missing number
            else:
                missing_ranges.append([prev + 1, num - 1])  # Range of missing numbers
        prev = num  # Update previous
        
    print(missing_ranges)

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)

clues = [-1]
lower = -1
upper = -1
find_missing_clues(clues, lower, upper)