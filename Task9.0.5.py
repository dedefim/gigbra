class Stationery:
    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print(f'Я простой рисунок: {self.title}')


class Pen(Stationery):
    def draw(self):
        return f'Я рисунок ручкой: {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Я рисунок карандашом: {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Я рисунок маркером: {self.title}'


stat = Stationery()
stat.draw()
pen = Pen()
print(pen.draw())
pencil = Pencil()
print(pencil.draw())
handle = Handle()
print(handle.draw())
