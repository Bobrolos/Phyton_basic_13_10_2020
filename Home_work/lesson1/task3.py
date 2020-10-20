"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
"""

number_n = int(input("Введите число n\n>>>: "))
sumnumber = number_n + int(str(number_n)*2) + int(str(number_n)*3)
print("суммa чисел n + nn + nnn:", sumnumber)
