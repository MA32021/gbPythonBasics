# 2. Реализовать класс Road (дорога).
#
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    # задаим параметры по умолчанию как аттрибуты класса Road
    _length = 5000
    _width = 20
    _cost = 25
    _roadbed_thickness = 5

    def __init__(self, length=_length, width=_width):
        """ Инициализатор класса

        :param length: по умолчанию равен аттрибуту класса Road._length
        :param width: по умолчанию равен аттрибуту класса Road._width
        """
        self._length = length
        self._width = width

    def calc_asfalt(self, cost=_cost, roadbed_thickness=_roadbed_thickness):
        """ Метод расчета массы асфальта

        :param cost: удельные затраты асфальта на 1 кв.м толщиной 1 см, по умолчанию равен Road._cost
        :param roadbed_thickness: толщина покрытия, по умолчанию равен Road._roadbed_thickness
        :return: рассчитанное значение массы асфальта
        """
        return self._width * self._length * cost * roadbed_thickness


some_road = Road(length=1000, width=25)
print(some_road.calc_asfalt(30, 3))
