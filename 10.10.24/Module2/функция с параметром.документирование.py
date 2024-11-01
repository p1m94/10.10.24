def say_hello(name):
    print('Hello', name)
# Принимающая функция
say_hello('Denis')
say_hello('Vlad')
say_hello('Dima')
# Возвращающая функция
import random
def lottery(mon, thue):
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    win3 = random.choice(tickets)
    print(mon, thue)
    return win1, win2

win1, win2 = lottery(mon: 'mon', thue: 'thue')