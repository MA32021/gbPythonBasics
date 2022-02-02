# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

# генерируем набор из 100 псевдослучайных чисел от 0 до 100
some_numbers = [randint(0, 100) for num in range(100)]

# записываем набор чисел, разделеных пробелами, в файл lesson-5-5-file.txt
with open('lesson-5-5-file.txt', 'w') as lesson5_file:
    print(*some_numbers, sep=' ', file=lesson5_file)

# считываем числа из файла и выводим их сумму
with open('lesson-5-5-file.txt', 'r') as lesson5_file:
    content = lesson5_file.read()
    print(f'Общая сумма чисел в файле равна: {sum([int(s) for s in content.split()])}')

