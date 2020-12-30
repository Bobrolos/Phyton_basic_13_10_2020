"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

class Org_technic:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity}
    def __str__(self):
        return f'Модель - {self.name}, цена - {self.price}, количество - {self.quantity}.'

    def input_store(self):
        try:
            unit_name = input(f'Введите наименование >>>')
            unit_price = int(input(f'Введите цену >>>'))
            unit_quantity = int(input(f'Введите количество >>>'))
            unit_data = {'Модель устройства': unit_name, 'Цена за ед': unit_price, 'Количество': unit_quantity}
            self.my_unit.update(unit_data)
            self.my_store.append(self.my_unit)
        except ValueError:
            return f'Ошибка ввода'

#    def Restore_to(self):


class Printer(Org_technic):
    def to_print(self):
        return f'{self.name} это принтер'

class Scanner(Org_technic):
    def to_scan(self):
        return f'{self.name} это сканер'

class Copier(Org_technic):
    def to_scan(self):
        return f'{self.name} это сканер'


my_org = Printer("HP-1000", 4800, 6)
print(my_org.to_print())