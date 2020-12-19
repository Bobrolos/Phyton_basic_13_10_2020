"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open("Task2_text.txt", 'r', encoding="utf-8") as f_obj:
    num_lines = 0
    num_words = 0
    for line in f_obj:
        words = line.split()
        num_lines += 1
        num_words += len(words)
        print(f'Количество слов в строке № {num_lines} - {num_words}')
    print(f'Общее количество строк - {num_lines}')
"""
sum_string = sum(1 for line in open("Task2_text.txt", 'r', encoding="utf-8"))
print(f'Количество строк - {sum_string}')
"""
f_obj.close()
