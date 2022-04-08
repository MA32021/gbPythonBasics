# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

import traceback


class MatricesRangesMismatch(Exception):
    def __init__(self, m1=None, m2=None):
        """ Конструктор может принять объекты, чтобы выввести
        в сообщении об ошибке, в каких матрицах несовпадают ранги

        :param m1: первая матрица
        :param m2: вторая матрица
        """
        if m1 is not None and m2 is not None:
            self.err_msg = f'Ranges of <{self.__get_obj_name(m1)}> and <{self.__get_obj_name(m2)}> do not match'
        else:
            self.err_msg = 'Matrices ranges mismatch'
        super().__init__(self.err_msg)

    def __str__(self):
        return self.err_msg

    @staticmethod
    def __get_obj_name(obj):
        """Приватный статический метод (ему не нужен self)
        возвращает имя объекта
        используется для вывода доп. информации об исключении

        :param obj: объект
        :return: имя переменной - экземпляра объекта
        """
        for name, item in globals().items():
            if item == obj:
                return name


class Matrix:
    def __init__(self, lst):
        """ Конструктор класса Matrix
        Проверяет входной список и если это непустой двухмерный массив,
        то инициализирует аттрибуты elements, вычисляет ранг матрицы и записывает его
        в аттрибут - список self.range
        Иначе - генерируется исключение класса IllegalMatrix

        :param lst: двухмерный массив
        """
        if not type(lst) == list or len(lst) == 0:
            self.range = [0, 0]
            self.elements = None
            raise ValueError('Attempt to create null ot illegal matrix')
        else:
            ranges = [len(i) for i in lst]
            if min(ranges) == max(ranges):
                self.elements = lst
                self.range = [len(lst), 0 if type(lst[0]) is not list else len(lst[0])]
            else:
                self.range = [0, 0]
                self.elements = None
                raise ValueError('Attempt to create null ot illegal matrix')

    def __str__(self):
        s = ''
        if self.elements is None:
            return 'None'
        for col in self.elements:
            for row in col:
                s = s + str(row) + ' '
            s = s[:len(s) - 1] + '\n'
        return s[:len(s) - 1]

    def is_matching(self, other):
        """ Метод для сравнения ранга матриц

        :param other: объект класса matrix для сравнения рангов (аттрибутов range)
        :return: True если ранг матриц совпадает
        """
        return self.range == other.range

    def __add__(self, other):
        if not self.is_matching(other):
            raise MatricesRangesMismatch(self, other)
        addition = []
        for r in range(self.range[0]):
            addition.append([self.elements[r][c] + other.elements[r][c] for c in range(self.range[1])])
        return Matrix(addition)


matrix1 = Matrix([[31, 32], [37, 43], [51, 86]])
print('Матрица 1:', matrix1, sep='\n')
matrix2 = Matrix([[1, 2], [7, 3], [1, 6]])
print('Матрица 2:', matrix2, sep='\n')
print('Результат сложения матриц 1 и 2:', matrix1 + matrix2, sep='\n')

# пример создания пустой матрицы
try:
    matrix6 = Matrix([])
except ValueError:
    print('Ошибка при попытке создания пустой матрицы')
    print(traceback.format_exc())

# пример создания кривой матрицы
try:
    matrix7 = Matrix([[1, 2, 3], [1]])
except ValueError:
    print('Ошибка при попытке создания кривой матрицы')
    print(traceback.format_exc())

# пример исключения, когда ранги матриц не совпадают
matrix4 = Matrix([[1, 2, 3], [7, 3, 0], [1, 6, 3]])
try:
    matrix5 = matrix1 + matrix4
except MatricesRangesMismatch as mrm_err:
    print('Ошибка при попытке сложения матриц:')
    print(mrm_err)
else:
    print(matrix5)
