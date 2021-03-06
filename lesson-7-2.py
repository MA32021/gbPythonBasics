# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        # у пальто - только размер
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, tall):
        # у костюма - только рост
        self.tall = tall

    @property
    def fabric_consumption(self):
        return 2 * self.tall + 0.3


coat1 = Coat(20)
print(f'Расход ткани на пальто: {round(coat1.fabric_consumption,2)}')
suit1 = Suit(4)
print(f'Расход ткани на костюм: {round(suit1.fabric_consumption,2)}')
print(f'Общий расход ткани: {round(coat1.fabric_consumption + suit1.fabric_consumption,2)}')
