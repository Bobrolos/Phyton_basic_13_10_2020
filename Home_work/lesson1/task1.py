"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""

some_var: int = 1
some_var_float: float = 24.976
some_var_string: str = "Hello"
name : str = "Имя"

print(some_var)
print(some_var_float)
print(some_var_string)
print(name)

name = input("Введите ваше имя\n>>>: ")
some_var_float = input("Введите дробное число\n>>>: ")
some_var = input("Введите целое число\n>>>: ")
print("Уважаемый(ая)", name, "Введённое Вами число:", some_var, ", верно?", sep=' ')
