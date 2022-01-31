# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_power(x, y):
    """Фукнция возведения в степень с использованием оператора **

    :param x: оснвоание
    :param y: показатель степени
    :return: результат возведения x в cntgtym y

    """
    return x ** y


def my_power_cycle(x, y):
    """Фукнция возведения в степень с использованием цикла

    :param x: оснвоание
    :param y: показатель степени
    :return: результат возведения x в степень y

    """
    if x == 0 and y < 0:
        raise ZeroDivisionError
    if y == 0:
        return 1
    res = x if y > 0 else 1 / x
    for n in range(1, abs(y)):
        res *= x if y > 0 else 1 / x
    return res


def my_power_recourse(x, y):
    """Фукнция возведения в степень с использованием рекурсии

    :param x: оснвоание, действительное число
    :param y: показатель степени, целое число
    :return: результат возведения x в степень y

    """
    if x == 0 and y < 0:
        raise ZeroDivisionError
    if y == 0:
        return 1
    if y == 1:
        return x
    elif y == -1:
        return 1 / x
    elif y < 0:
        return 1 / x * my_power_recourse(x, y + 1)
    else:
        return x * my_power_recourse(x, y - 1)


try:
    basis = float(input('Введите основание степени: '))
    exponent = int(input('Введите показатель степени: '))
    print("{:.20f}".format(basis ** exponent))
    print("{:.20f}".format(my_power_cycle(basis, exponent)))
    print("{:.20f}".format(my_power(basis, exponent)))
    print("{:.20f}".format(my_power_recourse(basis, exponent)))
except ZeroDivisionError:
    print('ОШИБКА при попытке возведения 0 в отрицательную степень')
except ValueError:
    print('Введен недопустимый тип данных')
