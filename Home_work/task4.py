'''
4. Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное,
выводить только первые 10 букв в слове.
'''
var_str = input("Введите строку\n>>>: ")
var_word = []
var_num = 1

var_word = var_str.split(' ')
for var_num, letter in enumerate(var_word, 1):
    if len(letter) > 10:
        letter = letter[0:10]
    print(f"{var_num}. - {letter}")
