while True:
    number = int(input('Введите число первого цикла: '))
    if number % 2 == 0:
        print('Число чётное')
    else:
        print('Число нечётное')
        break  # конец цикла

while True:
    number = int(input('Введите число второго цикла: '))
    if number == 23:
        break
    elif number % 2 == 0:
        print('Число чётное')
    else:
        print('Число нечётное')
    print('Я за отработал в обоих случаях')

while True:
        number = int(input('Введите число третьего цикла: '))
        if number % 2 == 0:
            print('Число чётное')
            continue # не даст отработать строчке  print('Я за отработал в обоих случаях')
        elif number == 13:
            break
        else:
            print('Число нечётное')
        print('Я отработал только в одном случае')
print('Конец циклов')