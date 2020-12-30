"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""
class Only_numbers(Exception):
    def __init__(self, txt):
        self.txt = txt
my_list = []
while True:
    number = input('Введите значение и нажмите Enter, для выхода нажмите Y - ')
    if number == "Y":
        print("Завершение ввода")
        break
    try:
        isnumber = int(number)
        my_list.append(isnumber)
    except ValueError:
        print("Вы ввели не число")
    except Only_numbers as err:
        print(err)
    else:
        print(f"Всё хорошо, введены только числа: {my_list}")
