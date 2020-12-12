"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_devider (*numbers):
    number1 = input("Введите делимое число\n>>>: ")
    while number1.isnumeric() == False:
        number1 = input("Введите число!\n>>>: ")
    number2 = input("Введите делитель\n>>>: ")
    while number2 == "0" or number2.isnumeric() == False:
        if number2 == "0":
            a = "Введите число не равное 0!"
        else:
            a = ''
        number2 = input(f"Введите другое число! {a} \n>>>: ")
    number1 = float(number1)
    number2 = float(number2)
    result = number1 / number2
    return result
print(f'результат деления - {my_devider()}')

