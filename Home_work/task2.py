"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. 4
Для заполнения списка элементов необходимо использовать функцию input().
"""

var_list = []
a = ""
list_long = 0
while a !="Y":
    var_list.append(input("Введите значение списка \n>>>: "))
    list_long = list_long + 1
    a = input("Нажмите Y, чтобы завершить ввод, либо любую клавишу для продолжения:")
    if a == "Y":
        break

i = 0

for item in var_list:
    if int(list_long) % 2 == 0:
        var_list[i], var_list[i + 1] = var_list [i + 1], var_list[i]
        i +=2
        if i >= list_long:
            break
    else:
        var_list[i], var_list[i + 1] = var_list[i + 1], var_list[i]
        i += 2
        if i >= list_long-1:
            break
print(var_list)
