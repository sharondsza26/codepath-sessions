# Problem 6: Cruise Ship Treasure Hunt
# As a fun game, the cruise ship director has organized a treasure hunt for the kids on board and hidden a chest of candy in one of the rooms on board. The rooms are organized in a m x n grid, where each row and each column are sorted in ascending order by room number. Given an integer representing the room number where the prize is hidden treasure, use a divide and conquer approach to return a tuple in the form (row, col) representing the row and column indices where treasure was found. If treasure is not in the matrix, return (-1, -1).

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_treasure(matrix, treasure):
    if not matrix or not matrix[0]:
        return (-1, -1)
    
    def search(row, col):
        if row >= len(matrix) or col < 0:
            return (-1, -1)
        
        current = matrix[row][col]
        if current == treasure:
            return (row, col)
        elif current > treasure:
            return search(row, col - 1)  # move left
        else:
            return search(row + 1, col)  # move down
    
    return search(0, len(matrix[0]) - 1)
# Example Usage:

rooms = [
    [1, 4, 7, 11],
    [8, 9, 10, 20],
    [11, 12, 17, 30],
    [18, 21, 23, 40]
]

print(find_treasure(rooms, 17))
print(find_treasure(rooms, 5))
# Example Output:

# (2, 2)
# (-1, -1)