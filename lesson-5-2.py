# 2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

# посчитаем количество строк и слов в файле 'lesson-5-2-file.txt'

with open('lesson-5-2-file.txt', 'r') as some_file:
    content = some_file.readlines()

print(f'Количество строк в файле: {len(content)}')

words = 0
for line in content:
    words = words + len(line.split())

print(f'Количество слов в файле: {words}')
