# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки для класса Stationery')


class Pen(Stationery):

    def __init__(self):
        Pen.title = 'Ручка'

    def draw(self):
        print(f'Рисует {Pen.title}')


class Pencil(Stationery):

    def __init__(self):
        Pencil.title = 'Карандаш'

    def draw(self):
        print(f'Чертит {Pencil.title}')


class Handle(Stationery):

    def __init__(self):
        Handle.title = 'Маркер'

    def draw(self):
        print(f'Выделяет {Handle.title}')


items = [Pen(), Pencil(), Handle()]

for item in items:
    item.draw()
