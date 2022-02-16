# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;

# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def show_speed(self):
        print(f'{self.name} едет со скоростью: {self.speed}')

    def go(self, speed):
        self.speed = speed
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')


class TownCar(Car):
    def __init__(self, name, color='black', speed=60):
        super().__init__('TownCar ' + name, color, speed, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость!', end=' ')
        super().show_speed()


class WorkCar(Car):
    def __init__(self, name, color='yellow', speed=40):
        super().__init__('WorkCar ' + name, color, speed, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает скорость!', end=' ')
        super().show_speed()


class SportCar(Car):
    def __init__(self, name, color='red&white', speed=120):
        super().__init__('SportCar ' + name, color, speed, False)


class PoliceCar(Car):
    def __init__(self, name, color='blue&yellow', speed=140):
        super().__init__('PoliceCar ' + name, color, speed, True)


car_1 = SportCar('Lightning McQueen', 'red', 180)
car_2 = TownCar('Luigi', 'yellow', 55)
car_3 = WorkCar('Guido', 'custom blue', 50)
car_4 = PoliceCar('Sheriff', 'black')

car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_3.go(35)
car_4.show_speed()
car_1.turn('налево')
car_1.stop()
car_4.turn('направо')
print(f'У {car_1.name} цвет {car_1.color}')
print(f'У {car_2.name} цвет {car_2.color}')
print(f'У {car_3.name} цвет {car_3.color}')
print(f'У {car_4.name} цвет {car_4.color}')
car_2.go(70)
print(f'{car_2.name} - это {"" if car_2.is_police else "не "}полицейская машина')
print(f'{car_4.name} - это {"" if car_4.is_police else "не "}полицейская машина')
