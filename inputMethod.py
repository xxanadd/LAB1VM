import re
import random


# Выбор метода ввода
def inputMethod():
    while True:
        try:
            inputMethod = int(input(
                'Выберите способ ввода 0-Пользовательский ввод; 1-Ввод данных из файла; 2-Генерация случайных матриц.\n'))
        except ValueError:
            print('Неправильно введены данные, попробуйте еще раз')
        else:
            if inputMethod < 0 or inputMethod > 2:
                print('Неправильно введены данные, попробуйте еще раз')
            else:
                break

    # Ввод из консоли
    if inputMethod == 0:

        # Выбор размерности матрицы
        while True:
            try:
                sizeI = int(input('Введите число строк:\n'))
            except ValueError:
                print('Допустимы только целочисленные значения')
            else:
                if sizeI <= 0:
                    print('Допустимы только значения > 0')
                else:
                    break
        sizeJ = sizeI + 1

        # Создание и заполнение матрицы числами
        matrix = [[0] * sizeJ for i in range(sizeI)]
        for i in range(sizeI):
            while True:
                line = input('Введите строку ' + str(i + 1) + '\n')
                if re.search(r'\.', line):
                    print('Дроби вводятся через запятую')
                    continue
                if re.search(r',,', line):
                    print('Неправильно введены данные, попробуйте еще раз')
                    continue
                line = line.replace(',', '.')
                line = line.split(' ')
                if len(line) != sizeJ:
                    print('Количество введенных значений не соотвтетствует допустимому')
                    continue
                for cell in range(len(line)):
                    try:
                        line[cell] = float(line[cell])
                    except ValueError:
                        print('Неправильно введены данные, попробуйте еще раз')
                        break
                else:
                    matrix[i] = line
                    break
                continue
        return matrix

    # Ввод из файла
    if inputMethod == 1:
        while True:
            path = input('Введите полный путь до файла\n')
            try:
                file = open(path, 'r')
            except FileNotFoundError:
                print('Файл не найден')
            else:
                try:
                    sizeI = int(file.readline())
                except ValueError:
                    print('Допустимы только целочисленные значения')
                    continue
                else:
                    if sizeI <= 0:
                        print('Допустимы только количества строк > 0')
                        continue
                    sizeJ = sizeI + 1
                    matrix = [[0] * sizeJ for i in range(sizeI)]
                    lines = []
                    for line in file:
                        lines.append(line.strip())
                    if len(lines) != sizeI:
                        print('Указано неверное количество строк')
                        continue
                    for i in range(len(lines)):
                        if re.search(r'\.', lines[i]):
                            print('Дроби вводятся через запятую')
                            break
                        if re.search(r',,', lines[i]):
                            print('Слишком много запятых')
                            break
                        lines[i] = lines[i].replace(',', '.')
                        matrix[i] = lines[i].split(' ')
                        if len(matrix[i]) != sizeJ:
                            print('Неправильное количество столбцов')
                            break
                        try:
                            for j in range(len(matrix[i])):
                                matrix[i][j] = float(matrix[i][j])
                        except ValueError:
                            print('Неправильно введен формат данных, попробуйте еще раз')
                            break
                    else:
                        return matrix
                        break
                    continue
    if inputMethod == 2:
        while True:
            try:
                sizeI = int(input('Введите число строк:\n'))
            except ValueError:
                print('Допустимы только целочисленные значения')
            else:
                if sizeI <= 0:
                    print('Допустимы только значения > 0')
                else:
                    break
        sizeJ = sizeI + 1
        unknownValues = []
        for value in range(sizeI):
            unknownValues.append(round(random.uniform(-100.00, 100.00), 2))
        matrix = [[0] * sizeJ for i in range(sizeI)]
        for line in matrix:
            equation = 0
            for cell in range(len(line) - 1):
                line[cell] = round(random.uniform(-100.00, 100.00), 2)
                equation += line[cell] * unknownValues[cell]
            line[sizeJ - 1] = round(equation, 4)
        return matrix
