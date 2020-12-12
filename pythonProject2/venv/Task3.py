"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def max_sum_func(var_1, var_2, var_3):
    numbers_sorted = sorted([var_1, var_2, var_3])
    return numbers_sorted[-1] + numbers_sorted[-2]
print(max_sum_func(90, 40, 60))
