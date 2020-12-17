"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

try:
    n = int(input("Введите число >>>"))
except ValueError:
    print('Введите корректное число!')

def fact(n):
    if n == 1:
        yield 1
    else:
        yield from (i * n for i in fact(n - 1))

for el in fact(n):
    print(f'Факториал {n}: {el}')
    if n == 15:
        break
    n += 1