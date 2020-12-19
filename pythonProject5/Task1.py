"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
out_f = open("out_file.txt", "w", encoding="utf-8")
str_list = input("Введите данные, либо введите пустую строку для окончания ввода данных \n>>>")

while str_list != "":
    out_f.writelines(str_list)
    str_list = input('Введите данные, либо введите пустую строку для окончания ввода данных \n>>>')
out_f.close()

out_f = open("out_file.txt", 'r', encoding="utf-8")
content = out_f.readlines()
print(content)
out_f.close()
