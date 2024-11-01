tuple_ = 1, 2, 3, True, 'Hot'
print(tuple_)
tuple_2 = ([1,2],3,4)
tuple_2[0][1] = 'cold' # замена второго элемента в первом (списке) кортежа на символ 3
print(tuple_2)



print('Начало практического задания')
immutable_var = 1, 2, True, 'Кортеж'
print(immutable_var)
print(type(immutable_var))
mutable_list = [1, 2, True, 'Список'] # Список находится в квадратных скобках
print(mutable_list)
mutable_list[0] = 10
mutable_list[1] = 20
mutable_list[2]= False
mutable_list[3]= 'Спать'
print(mutable_list)
print(type(mutable_list))