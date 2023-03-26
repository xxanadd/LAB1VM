def determinant(matrix):
    det = 1
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det
