# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, str_date):
        if Date.validate_date(str_date):
            dmy = Date.retrieve_date(str_date)
            self.day = dmy[0]
            self.month = dmy[1]
            self.year = dmy[2]
        else:
            self.day = None
            self.month = None
            self.year = None

    @classmethod
    def retrieve_date(cls, str_date):
        """ Выделяет дату из входной строки
        и помещает день, месяц, год, разделенные '-',
        в список из трех целых чисел
        :param str_date: дата в формате дд-мм-гггг
        :return: список [номер дня, номер месяца, номер года]
        или пустой список, если формат неверен
        """
        try:
            ddmmyy = str_date.split('-')
            int_date = [int(el) for el in ddmmyy]
        except ValueError:
            return []
        else:
            return int_date

    @staticmethod
    def validate_date(str_date):
        """ Проверяет дату в виде строки в формате дд-мм-гггг

        :param str_date: строка с датой в формате дд-мм-гггг
        :return: True, если дата правильная, иначе - False
        """
        ddmmyy = Date.retrieve_date(str_date)
        # если список ddmmyy не содержит три элемента, то False
        if len(ddmmyy) != 3:
            return False
        # словарь количества дней в месяце
        mdays = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        try:
            # если високосный год, то в феврале может быть 29 дней
            if not ddmmyy[2] % 4:
                mdays[2] = 29
            return (ddmmyy[0] in range(1, mdays[ddmmyy[1]] + 1)) and (ddmmyy[1] in range(1, 13))
        except KeyError:
            return False


print(Date.validate_date('03-12-15'))
print(Date.validate_date('29-02-1981'))

some_date = Date('01-03-1970')
print(some_date.day, some_date.month, some_date.year)
another_date = Date('29-02-1970')
print(another_date.day, another_date.month, another_date.year)