import time


class TrafficLight:

    def running(self):
        self._color = 'Красный'
        print(f'{self._color}')
        time.sleep(7)
        self._color = 'Жёлтый'
        print(f'{self._color}')
        time.sleep(2)
        self._color = 'Зелёный'
        print(f'{self._color}')
        time.sleep(7)

trafic = TrafficLight()
trafic.running()
