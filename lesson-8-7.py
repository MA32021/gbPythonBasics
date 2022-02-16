# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complexus:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complexus(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complexus(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complexus(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __truediv__(self, other):
        return Complexus((
                                 self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2), (
                                 self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2))

    def __str__(self):
        return f'({self.a}{"+" if self.b > 0 else ""}{self.b}j)'


n1 = Complexus(2, 5)
print(n1)
print(complex(2, 5))
n2 = Complexus(3, -4)
print(n2)
print(complex(3, -4))
# проверяем деление
print(n1 / n2)
print(complex(2, 5) / complex(3, -4))
# проверяем сложение
print(n1 + n2)
print(complex(2, 5) + complex(3, -4))
# проверяем умножение
print(n1 * n2)
print(complex(2, 5) * complex(3, -4))
# проверяем вычитание
print(n1 - n2)
print(complex(2, 5) - complex(3, -4))
