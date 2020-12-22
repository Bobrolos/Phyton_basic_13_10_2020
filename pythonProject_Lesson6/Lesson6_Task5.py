"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationary):
    def draw(self):
        return f'Вы используете {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def draw(self):
        return f'Вы используете {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def draw(self):
        return f'Вы используете {self.title}. Запуск отрисовки маркером'

my_pen = Pen('Красная ручка')
my_pencil = Pencil('Синий карандаш')
my_handle = Handle('Водостойкий маркер')
print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())