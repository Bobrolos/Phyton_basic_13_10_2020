"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
a = ""
i = 1
while a !="Y":
    new =  int(input("Введите новый элемент рейтинга \n>>>: "))
    max_value = max(my_list)
    if new > max_value:
        my_list.insert(0, new)
    elif new in my_list:
        my_list.insert(-my_list[::-1].index(new), new)
    else:
        my_list.append(new)
    print(my_list)
    a = input("Нажмите Y, чтобы завершить ввод, либо любую клавишу для продолжения:")
    if a == "Y":
        break