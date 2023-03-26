from decimal import Decimal


def discrepancy(matrix, results):
    variables = len(matrix)
    discrepancies = []
    for i in range(variables):
        summ = 0
        for j in range(variables):
            summ += Decimal(str(matrix[i][j]))*Decimal(str(results[j]))
        a = str(matrix[i][variables])
        b = str(summ)
        discrepancies.append(str(abs(Decimal(a) - Decimal(b))))
    return discrepancies
