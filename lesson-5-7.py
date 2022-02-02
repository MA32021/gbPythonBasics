# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
#
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

from statistics import mean
from json import dump, load

result = []
profits = {}
avg_profit = {}

with open('lesson-5-7-input.txt', 'r', encoding='utf-8') as fin_results:
    content = fin_results.readlines()

for row in content:
    cells = row.split()
    profits.update({cells[0]: float(cells[2]) - float(cells[3])})

result.append(profits)
result.append({'average_profit': mean([i for i in profits.values() if i > 0])})

with open('lesson-5-7-output.txt', 'w', encoding='utf-8') as out_file:
    dump(result, out_file)

# Код для проверки десериализации списка:
# test = []
# with open('lesson-5-7-output.txt', 'r', encoding='utf-8') as out_file:
#     test = load(out_file)
# print(test)
