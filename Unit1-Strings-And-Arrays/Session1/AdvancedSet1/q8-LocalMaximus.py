# Problem 8: Local Maximums
# Write a function local_maximums() that accepts an n x n integer matrix grid and 
# returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

# local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered 
# around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

def local_maximums(grid):
    n = len(grid)
    maxes = []
    for i in range(1, n-1):
        row_maxes = []
        for j in range(1, n-1):
            sub_matrix = [
                grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                grid[i][j-1],   grid[i][j],   grid[i][j+1],
                grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
            ]
            row_maxes.append(max(sub_matrix))
            
        maxes.append(row_maxes)
        
    print(maxes)

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
local_maximums(grid)

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
local_maximums(grid)