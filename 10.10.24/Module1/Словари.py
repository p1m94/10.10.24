# работа со словарями
my_dict = {'Linkin Park' : True, 'SOAD' : True, 'SlipKnot': True, 'Shaman': False}
print(type(my_dict), my_dict)
print(my_dict['Linkin Park']) # Вывод на экран значения ключа
print(my_dict.get('Falling in reverse')) # Вывод нахождения в словаре ключа
my_dict.update({'Metallica': True, 'Bullet for my valentine': True}) # Добавление в словарь ключей со значениями
print(my_dict)
my_dict.pop('Shaman') # Удаление ключа
print(my_dict)
# работа со множествами

my_set = {1, 2, 3, 1, 2, 3, True, True, False, False, 'Fox', 'Fox', 'fox'}
print(type(my_set), my_set)
my_set.discard('Fox')
print(my_set)