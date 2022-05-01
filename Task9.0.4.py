class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} {self.color}')

    def go(self):
        return f'{self.name}: поехала'

    def stop(self):
        return f'{self.name}: остановилась'

    def turn(self, direction):
        return f'{self.name}: повернула на {direction}'

    def show_speed(self):
        return f'{self.name}: Скорость = {self.speed}'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name} {self.speed}' ' Превышение скорости ' \
            if self.speed > 60 else f'{self.name} {self.speed}'


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name} {self.speed}' 'Превышение скорости'\
            if self.speed > 40 else f'{self.name} {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar("Audi", "black", 80)
police_car.go()
print(police_car.show_speed())
print(police_car.turn('left'))
print(police_car.stop())

town_car = TownCar("Нива", "black", 90)
town_car.go()
print(town_car.show_speed())
print(town_car.turn('40 градусов по направлению к мэрии'))
print(town_car.stop())
