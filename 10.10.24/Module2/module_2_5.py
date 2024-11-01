def get_matrix(n, m, value):
    matrix = [] # Пустой список для матрицы
    for i in range(n): # Внешний цикл для строки
        row = []    # Пустой список для строки
        for j in range(m): # Внутренний цикл для столбцов
            row.append(value) #  добавляем значение в строку
        matrix.append(row) # добавляем строку в матрицу
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)