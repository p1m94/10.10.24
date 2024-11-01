list_ = ['one', 'two', 'three']
list_2 = [2, 3, 4, 5, 1]
for i in list_:
    if i == 'three':
        list_.remove(i)
print(list_)

for i in range(5):
    print(i)
print(list_)

for i in range(len(list_)):
    list_[i] = ':(' # замена элемента
print(list_)

sum_ = 0
for i in range(len(list_2)):
    sum_ += list_2[i]
print(sum_) # cложить все элементы в списке

for i in range(1, 11, 2): #(start, stop, step)
    print((i))

for i in range(1, 11):  # (start, stop, step) #в конце идёт выполнение внешнего цикла
    for j in range(1, 11): # сначала идёт выполнение внутреннего цикла
        print(f'{i} x {j} = {i * j}') # f'' это функция

dict_ = {'a': 1, 'b': 2, 'c': 3}
for i, k in dict_.items():
    print(i, k)