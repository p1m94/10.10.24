def generate_password(first_num):
    result = ""
    pairs = []

    # Генерируем уникальные пары чисел
    for i in range(1, first_num):
        for j in range(i + 1, first_num):  # j начинается с i + 1 для уникальности
            pairs.append((i, j))

    # Формируем пароль
    for i, j in pairs:
        total = i + j
        concatenated_number = int(f"{i}{j}")
        # Проверяем кратность n сумме пары
        if first_num % total == 0:
            result += f"{concatenated_number}"

    return result

# Ввод числа n от 3 до 20
first_num = int(input("Введите число (от 3 до 20): "))

# Проверка диапазона
if first_num < 3 or first_num > 20:
    print("Число должно быть в диапазоне от 3 до 20.")
else:
    password = generate_password(first_num)
    print(f"Пароль для {first_num}: {password}")