"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

file_name, hours, pay_per_hour, bonus = argv

try:
    hours, pay_per_hour, bonus = int(hours), float(pay_per_hour), float(bonus)
    salary = hours * pay_per_hour + bonus
    print(f'заработная плата сотрудника - {salary}')
except ValueError:
    print('Введите корректное число!')
