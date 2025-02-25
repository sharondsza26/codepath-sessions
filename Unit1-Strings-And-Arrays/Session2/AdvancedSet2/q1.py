# Problem 1: Matrix Addition
# Write a function add_matrices() that accepts to n x m matrices matrix1 and matrix2. 
# The function should return an n x m matrix sum_matrix that is the sum of the given matrices 
# such that each value in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.

def add_matrices(matrix1, matrix2):
    sum_matrix = []
    
    for i in range(len(matrix1)):
        sum_matrix.append([])
        for j in range(len(matrix2)):
            sum_matrix[i].append(matrix1[i][j] + matrix2 [i][j])
            
    print(sum_matrix)


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

add_matrices(matrix1, matrix2)
