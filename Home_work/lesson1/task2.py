"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
input_time_sec = int(input("Введите время в секундах\n>>>: "))
hh = input_time_sec // 3600
ss = input_time_sec % 60
mm = (input_time_sec % 3600) // 60

if hh < 10:
    hh = str(hh)
    hh = "0" + hh

if mm < 10:
    mm = str(mm)
    mm = "0" + mm

if ss < 10:
    ss = str(ss)
    ss = "0" + ss

full_time = f'{hh:>2}:{mm:>2}:{ss:>2}'
print(full_time)
