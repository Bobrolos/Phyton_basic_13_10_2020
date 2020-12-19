"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def summ():
    try:
        with open('file_5.txt', 'w+') as f_obj:
            line = input('Введите числа через пробел \n>>>')
            f_obj.writelines(line)
            numbers = line.split()
            print(f'Сумма чисел = {sum(map(int, numbers))}')
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Введите число!')
summ()
