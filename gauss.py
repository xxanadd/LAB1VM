import copy


def triangle(mat):
    matrix = copy.deepcopy(mat)
    for k in range(1, len(matrix)):
        for j in range(k, len(matrix)):
            while True:
                try:
                    m = matrix[j][k - 1] / matrix[k - 1][k - 1]
                except ZeroDivisionError:
                    for fix in range(j, len(matrix)):
                        if matrix[fix][k-1] != 0:
                            tmp = matrix[fix]
                            matrix[fix] = matrix[fix - 1]
                            matrix[fix - 1] = tmp
                            break
                    else:
                        print('Нет решений')
                        break
                    continue
                else:
                    break
            for i in range(len(matrix) + 1):
                matrix[j][i] = matrix[j][i] - (m * matrix[k - 1][i])
    return matrix


def calculation(mat):
    matrix = copy.deepcopy(mat)
    x = [0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        sum = 0
        for j in range(i + 1, len(matrix)):
            sum += matrix[i][j]*x[j]
        sum -= matrix[i][len(matrix)]
        x[i] = -sum/matrix[i][i]
    return x



