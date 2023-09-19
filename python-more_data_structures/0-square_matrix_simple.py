def square_matrix_simple(matrix=[]):
    square=[[n**2 for n in row]for row in matrix]
    return square
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]
]
new_matrix=square_matrix_simple(matrix)
print(new_matrix)
print(matrix)