def calculate_structure_sum(*args):
    total_sum = 0

    for data in args:
        if isinstance(data, int):  # Если это целое число
            total_sum += data
        elif isinstance(data, str):  # Если это строка
            total_sum += len(data)  # Добавляем длину строки
        elif isinstance(data, (list, tuple, set)):  # Если это список, кортеж или множество
            total_sum += calculate_structure_sum(*data)  # Рекурсивный вызов
        elif isinstance(data, dict):  # Если это словарь
             for key, value in data.items():  # Для каждой пары ключ-значение
                    total_sum += calculate_structure_sum(key, value)  # Включаем ключи и значения

    return total_sum

# Тестовая структура данных
data_structure = [
    [1, 2, 3],                           # Сумма: 1 + 2 + 3 = 6
    {'a': 4, 'b': 5},                    # Сумма: 1 (a) + 1 (b) + 4 + 5 = 11
    (6, {'cube': 7, 'drum': 8}),         # Сумма: 6 + 4 (cube) + 4 (drum) + 7 + 8 = 29
    "Hello",                              # Сумма: длина "Hello" = 5
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # Сумма: 2 + 5 (Urban) + 6 (Urban2) + 35
]

result = calculate_structure_sum(*data_structure)
print(result)