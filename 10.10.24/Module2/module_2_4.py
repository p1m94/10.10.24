numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = [] # Создаем пустые списки для простых и непростых чисел
not_primes = []

for num in numbers:      # Перебираем каждый элемент в списке numbers
    is_prime = True     # Предполагаем, что число простое
    if num < 2:          # Числа меньше 2 не являются простыми
        is_prime = False

    for i in range(2, int(pow(num, 0.5) + 1)): # Проверка делителей от 2 до pow((x), 0.5)) - Функция получения квадратного корня и округление его до следующего целого числа после себя самого
        if num % i == 0:  # Если есть делитель
            is_prime = False
            break  # Выход из цикла, так как число не простое

    if is_prime:
        prime.append(num)  # Добавляем число в соответствующий список
    else:
        not_primes.append(num) # Добавляем остальные числа в соответствующий список

print("Простые числа:", prime)
print("Непростые числа:", not_primes)