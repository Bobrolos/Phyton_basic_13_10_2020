"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
 месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def extract_from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        date = cls(day, month, year)
        return date

    @staticmethod
    def check_date_valid(date_string):
        day, month, year = map(int, date_string.split('-'))
        if day <= 31 and month <= 12 and year <= 3999:
            return "Дата корректна"
        else:
            return "Введите корректную дату!"

my_date = Date.extract_from_string('30-12-2020')
my_isdate = Date.check_date_valid('11-23-2056')

print(my_date.extract_from_string('30-12-2020'))
print(my_isdate)
