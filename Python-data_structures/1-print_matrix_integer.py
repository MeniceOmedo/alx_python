def print_matrix_interger(matrix=[[]]):
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    for x in matrix:
        for y in x:
            print(y,end="\t")
        print()
    
print(print_matrix_interger()) 