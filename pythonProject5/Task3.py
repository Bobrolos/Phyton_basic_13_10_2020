"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

with open("Task3_text.txt", 'r', encoding="utf-8") as f_obj:
    count_people = 0
    count_salary = 0
    for line in f_obj:
        words = line.split()
        if int(words[1]) < 20000:
            print(line)
        count_salary += int(words[1])
        count_people += 1
print(f'Средняя зарплата сотрудников - {count_salary / count_people}')
f_obj.close()
