# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numbers = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}

with open('lesson-5-4-input.txt', 'r') as src_file:
    content = src_file.readlines()

with open('lesson-5-4-output.txt', 'w', encoding='utf-8') as dst_file:
    for line in content:
        words = line.split()
        print(f'{numbers.get(int(words[2]))} {words[1]} {words[2]}', file=dst_file)