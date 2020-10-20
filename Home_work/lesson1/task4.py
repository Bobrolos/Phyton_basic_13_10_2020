"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""
int_number: int = int(input("Введите целое положительное число\n>>>: "))
max_number = int_number % 10
int_number = int_number // 10
while int_number != 0:
    if max_number < (int_number % 10):
                    max_number = int_number % 10
    int_number = int_number // 10
print("Самая большая цифра числа:", max_number)
