"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""
class Zero_devition(Exception):
    def __init__(self, txt):
        self.txt = txt

divider = input("Введите делимое: ")
number =  input("Введите делитель: ")

try:
    divider = int(divider)
    number = int(number)
    if number == 0:
        raise Zero_devition("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except Zero_devition as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {divider/number}")
