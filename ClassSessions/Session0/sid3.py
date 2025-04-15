def find_last_cell(N, M, matrix):
    top, bottom, left, right = 0, N - 1, 0, M - 1
    row, col = 0, 0  # Starting position
    visited = 0  # Count of cells visited

    while top <= bottom and left <= right:
        # Move right across the top row
        for col in range(left, right + 1, 2):
            visited += 1
            last_visited = matrix[row][col]  # Track the last visited cell
        top += 1
        
        # Move down along the right column
        for row in range(top, bottom + 1, 2):
            visited += 1
            last_visited = matrix[row][col]  # Track the last visited cell
        right -= 1
        
        # Move left across the bottom row
        for col in range(right, left - 1, -2):
            visited += 1
            last_visited = matrix[row][col]  # Track the last visited cell
        bottom -= 1
        
        # Move up along the left column
        for row in range(bottom, top - 1, -2):
            visited += 1
            last_visited = matrix[row][col]  # Track the last visited cell
        left += 1
    
    return last_visited  # Return the last cell Lucy hopped onto

# Input handling
N, M = map(int, input().split())  # Read matrix dimensions
matrix = [list(map(int, input().split())) for _ in range(N)]  # Read the matrix

# Output the last cell Lucy would hop onto
print(find_last_cell(N, M, matrix))
