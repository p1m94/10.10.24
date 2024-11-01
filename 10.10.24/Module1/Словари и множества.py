phone_book = {'Vladlen': 89135981282, 'Kris': [89130438782, 111]}
print(phone_book['Kris'])
phone_book['Anton']= 899999999 # добавил в словарь ключ со значением
del phone_book['Vladlen'] # удалил из словаря ключ
print(phone_book)
phone_book.update({'Sasha': 11111,
                   'Alex': 222222}) # Обновили словарь и внесли в него новые данные
print(phone_book.get('Kris')) # Получение значения по указанному ключу
print(phone_book)
a = phone_book.pop('Anton') # сохранение удаляемого ключа в перемённую а
list_ = [1,2,3]
list_.pop(0) # убрали элемент с индексом 0
print(list_)
print(phone_book)
print(a)

# метод keys позволяет получить коллекцию из ключей в словаре

print(phone_book.keys())
# метод values позволяет получить коллекцию из значений в словаре

print(phone_book.values())
# метод items позволяет получить коллекцию из  пар ключей и значений в словаре
print('ЗДЕСЬ',phone_book.items())
print(phone_book)

# Множества

set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4}
print(type(set_))
list_ = [1,1,2,1,2,1,2]
print(list_)
print(set(list_))
list_ = set(list_) # cделал из списка множество

print(list_)
print(list_.add(5))