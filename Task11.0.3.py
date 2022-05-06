import time
list_2 = []


class Stock:
    def __init__(self, quantity, name):
        self.quantity = quantity
        self.name = name

    def counter(self, counters):
        list_2.count(counters)
        return


class AgriculturalTechnology:

    def __init__(self, start='Начало работы', end='Работа завершена'):
        self.start = start
        self.end = end


class Printer(AgriculturalTechnology):

    def printed(self):
        print(f'{self.start}, начинаю печать')
        time.sleep(1)
        list_2.append('printer')
        return f'{self.end}, всё хорошо'


class Xerox(AgriculturalTechnology):

    def xeroxed(self):
        print(f'{self.start}, не открывайте крышку')
        time.sleep(1)
        list_2.append('xerox')
        return f'{self.end} :)'


class Scanner(AgriculturalTechnology):

    def scanning(self):
        print(f'{self.start}, будте осторожны')
        time.sleep(1)
        list_2.append('scanner')
        return f'{self.end} 100% выполнение'


xerox = Xerox
print(xerox.xeroxed)
stock = Stock
print(stock.counter(xerox))
