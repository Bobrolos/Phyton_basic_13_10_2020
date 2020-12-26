"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
# класс Count_fabric
class Count_fabric:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_fabric_1(self):
        return self.width / 6.5 + 0.5

    def count_fabric_2(self):
        return self.height * 2 + 0.3

    @property
    def count_all(self):
        return str(f'Общий расход ткани - {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Count_coat(Count_fabric):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто {self.square_c}'


class Count_jacket(Count_fabric):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм {self.square_j}'

print(Count_coat(2, 7))
print(Count_jacket(2, 7))
print(Count_fabric.count_all(2, 7))
