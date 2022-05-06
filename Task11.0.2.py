a = []
try:
    while a.count("stop") == 0:
        a = input('Введите данные: ')
        a = int(a)
except AttributeError:
    print(a)
except ValueError:
    print('Вы ввели не число :)')