# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

from random import sample


def comp_prev(lst):
    """Функция - генератор yield, который возвращает текущий элемент списка,
     если он больше предыдущего

    :param lst: список значений
    :return: элемент входного, который больше предыдущего
    """
    for i in range(1, len(lst)):
        try:
            if lst[i] > lst[i - 1]:
                yield lst[i]
        except:
            continue


# Генерируем случайный список десяти чисел от 0 до 100
some_list = sample(range(0, 100), 10)
print(f'Исходный список: {some_list}')

next_grater_lst = [el for el in comp_prev(some_list)]

print(f'Результат: {next_grater_lst}')
