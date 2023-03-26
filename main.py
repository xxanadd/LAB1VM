from inputMethod import inputMethod
from gauss import triangle
from gauss import calculation
from discrepancy import discrepancy
from det import determinant as det


def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i]) - 1):
            print('{:6g}'.format(round(mat[i][j], 3)), end=" ")
        print(' | ' + '{:6g}'.format(round(mat[i][j + 1], 3)), end=" ")
        print()


matrix = inputMethod()
print()
triangle = triangle(matrix)
det = det(triangle)
if det == 0:
    print('Определитель равен нулю, решений нет')
else:
    print('Определитель ' + str(det))
    calculation = calculation(triangle)
    print('\nВходная матрица')
    printMatrix(matrix)
    print('\nТреугольная матрица')
    printMatrix(triangle)
    print('\nВектор неизвестных')
    print(calculation)
    print('\nВектор невязок')
    print(discrepancy(matrix, calculation))
