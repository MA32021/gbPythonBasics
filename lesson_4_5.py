# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
#
# Подсказка: использовать функцию reduce().

# [AM's comment: лучше было бы рассчитать сумму всех элементов, так как результат произведения слишком длинный]

from functools import reduce


def multiply(prev_el, el):
    return prev_el * el


print(reduce(multiply, [n for n in range(100, 1001, 2)]))