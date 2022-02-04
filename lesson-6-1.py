# 1. Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы:
# красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться
# только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    _color = 'Красный'
    __red_delay = 7
    __yellow_delay = 2
    __green_delay = 5

    def running(self):
        """ Метод переключения состояния светофора
        Выводит текущее состояние, 
        после установленной задержки переключает его к следующему
        и выводит время задержки и новое состояние.
        ps. По идее за зеленым должен идти желтый,
        но по условию задания выше - сразу опять красный

        :return: void
        """
        print(f'{self._color} >> переключается за ', end='')
        if self._color == 'Красный':
            sleep(self.__red_delay)
            print(f'{self.__red_delay} сек. на', end=' ')
            self._color = 'Желтый'
        elif self._color == 'Желтый':
            sleep(self.__yellow_delay)
            print(f'{self.__yellow_delay} сек. на', end=' ')
            self._color = 'Зелёный'
        else:
            sleep(self.__green_delay)
            print(f'{self.__green_delay} сек. на', end=' ')
            self._color = 'Красный'
        print(f'>> {self._color}')


tl_1 = TrafficLight()
tl_1.running()
tl_1.running()
tl_1.running()
tl_1.running()
tl_1.running()
tl_1.running()
tl_1.running()
