"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
result= []
with open("Task4_text.txt", 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        numbers = line.split(" - ")
        if numbers[0] in rus:
            words = rus[numbers[0]]
            result.append(words + ' - ' + numbers[1])
    print(result)

with open('file_4_new.txt', 'w') as f_obj2:
    f_obj2.writelines(result)

f_obj2.close()
f_obj.close()
