class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, weidth=25, thickness=5):
       return f" Масса: {(self._width * self._length * weidth * thickness)}"


road = Road(5000, 200)
road.mass_calculation()
