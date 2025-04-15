# Problem 2: Counting the Castle Walls
# In a faraway kingdom, a castle is surrounded by multiple defensive walls, 
# where each wall is nested within another. Given a list of lists walls where each 
# list [] represents a wall, write a recursive function count_walls() that returns the 
# total number of walls.

# Evaluate the time complexity of your solution. Define your variables and provide a 
# rationale for why you believe your solution has the stated time complexity.

def count_walls(walls):
    if not walls:
        return 1
    
    return 1 + count_walls(walls[1])
# Example Usage:

walls = ["outer", ["inner", ["keep", []]]]

print(count_walls(walls))
print(count_walls([]))
# Example Output:

# 4
# 1