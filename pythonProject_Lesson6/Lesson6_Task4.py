"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. В
ыполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    # атрибуты класса
    speed = None
    color = None
    name = None
    is_police = None

    # методы класса
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return  f'{self.name} едет'
    def stop(self):
        return  f'{self.name} остановилась'
    def turn(self, direction):
        return f'{self.name} повернул {direction}'
    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')
        if self.speed > 40:
            return f'Текущая скорость {self.name} - {self.speed} - выше разрешённой'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')
        if self.speed > 60:
            return f'Текущая скорость {self.name} - {self.speed} - выше разрешённой'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police == True:
            return f'{self.name} - полицейская машина'

car_1 = SportCar('Audi', 70, 'Голубой', False)
car_2 = TownCar('Lexus', 40, 'Белый', False)
car_3 = WorkCar('Mercedes', 70, 'Чёрный', True)
car_4 = PoliceCar('Ford', 110, 'Красный', True)

print(car_1.name, car_1.color, car_1.speed)
print(car_3.go(), car_3.turn('Направо'), car_3.show_speed(), car_3.stop())
print(car_4.police())
