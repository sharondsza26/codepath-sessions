# Problem 1: Transpose Matrix
# Write a function transpose() that accepts a 2D integer array matrix and 
# returns the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, 
# swapping the rows and columns.

def transpose(matrix):
    transpose_matrix = []
    for i in range(len(matrix)):
        transpose_matrix.append([])
        for j in range(len(matrix[i])):
            transpose_matrix[i].append(matrix[j][i])
    
    return transpose_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# transpose(matrix)