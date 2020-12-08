"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""


month = int(input("Введите месяц в виде целого числа от 1 до 12\n>>>: "))
season_list = ("зима", "весна", "лето", "осень")
season_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето',
               8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

if month == 12 or month == 1 or month == 2:
    print(season_list[0])
    print(season_dict.get(month))
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
    print(season_dict.get(month))
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
    print(season_dict.get(month))
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
    print(season_dict.get(month))
else:
    print("Ошибка ввода!")
