# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

from statistics import mean

with open('lesson-5-3-file.txt', 'r', encoding='utf-8') as salaries:
    salaries_cont = salaries.readlines()

salaries_db = {}
for line in salaries_cont:
    pair = line.split()
    salaries_db.update({pair[0]: float(pair[1])})

print(f'Оклад менее 20 тысяч получают: {", ".join([key for key, val in salaries_db.items() if val < 20000])}')
print(f'Средняя величина дохода сотрудников: {round(mean(salaries_db.values()),2)}')
