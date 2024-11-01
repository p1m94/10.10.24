calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info(string):
    count_calls() # Увеличиваем счетчик вызовов
    lenght = len(string)
    UP_string = string.upper() # Строка в верхнем регистре
    LOW_string = string.lower() # Строка в нижнем регистре
    return (lenght, UP_string, LOW_string) # возвращаем кортеж

def is_contains(string, list_to_search):
    count_calls()
    string_low = string.lower()
    return any(item.lower() == string_low for item in list_to_search)



# Вызовы функций с произвольными данными
print(string_info('Capybara'))                # Вывод информации о строке
print(string_info('Armageddon'))               # Вывод информации о строке
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Проверка наличия строки в списке
print(is_contains('cycle', ['recycling', 'cyclic']))    # Проверка наличия строки в списке

# Выводим количество вызовов функций
print(calls)