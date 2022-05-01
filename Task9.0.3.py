class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._icome = {"profit": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f'{sum(self._icome.values())}'

manager = Position("Ivan", "Ivanov", "AAA", 10000000, 1)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())
