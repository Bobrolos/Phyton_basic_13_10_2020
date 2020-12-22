"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road:
    # атрибуты класса
    __length = None
    __width = None
    weigth = None
    tickness = None

    # методы класса
    def __init__(self, length, width, weight, tickness):
        self.length = length
        self.width = width
        self.weigth = weight
        self.tickness = tickness

    def road_count(self):
        road_count = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна - {road_count} тонн')

my_road = Road(5000, 20, 25, 5)
my_road.road_count()
