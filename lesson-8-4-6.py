# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from datetime import datetime
import traceback


class NotInStock(Exception):
    def __init__(self, item=None):
        if item is not None:
            self.err_msg = f'Устройства <{item.name}> #{item.id} нет на складе'
        else:
            self.err_msg = 'Устройства нет на складе'
        super().__init__(self.err_msg)


class StockDuplicate(Exception):
    def __init__(self, item=None):
        if item is not None:
            self.err_msg = f'Устройство <{item.name}> #{item.id} уже на складе'
        else:
            self.err_msg = 'Устройство уже на складе'
        super().__init__(self.err_msg)


class Stock:
    def __init__(self, name):
        self._name = name
        self.balance = 0
        self.items = {}
        self.log_book = []

    def add_item(self, item):
        try:
            if item in self.items.values():
                raise StockDuplicate(item)
        except StockDuplicate:
            print(traceback.format_exc())
        else:
            self.items.update({item.id: item})
            self.log_book.append(
                f'{datetime.now()}\tПоступление {item.type} <{item.name}> #{item.id} из <{item.location}>')
            item.location = self._name
            self.balance = len(self.items)

    def pass_item(self, item, pass_to):
        if self.balance != 0:
            try:
                if item not in self.items.values():
                    raise NotInStock(item)
            except NotInStock:
                print(traceback.format_exc())
            else:
                self.items[item.id].location = pass_to
                self.items.pop(item.id)
                self.balance = len(self.items)
                self.log_book.append(
                    f'{datetime.now()}\tВыбытие {item.type} <{item.name}> #{item.id} в <{item.location}>')

    def print_log(self):
        print('-' * 80)
        print(f'Журнал событий склада <{self._name}>')
        print('-' * 80)
        for rec in self.log_book:
            print(rec)
        print('-' * 80)

    def __str__(self):
        return f'Склад <{self._name}> содержит {self.balance} единиц хранения'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.log_book.append(f'{datetime.now()}\tСклад <{self.name}> сменил имя на <{value}>')
        self._name = value
        if self.balance != 0:
            for item in self.items.values():
                item.location = value


class Device:
    def __init__(self, item_id, name, location=''):
        self.id = item_id
        self.name = name
        self.location = location
        self.type = ''

    def __str__(self):
        return f'Устройство <{self.type}> номер {self.id} с именем <{self.name}> находится в <{self.location}> '


class Printer(Device):
    def __init__(self, item_id, name, location='', resource=10000):
        Device.__init__(self, item_id, name, location)
        self.type = 'Printer'
        self.resource = resource


class Scaner(Device):
    def __init__(self, item_id, name, location='', iscolour=False):
        Device.__init__(self, item_id, name, location)
        self.type = 'Scaner'
        self.iscolour = iscolour


class MFU(Device):
    def __init__(self, item_id, name, location='', features='psx'):
        Device.__init__(self, item_id, name, location)
        self.type = 'MFU'
        self.features = features


my_stock = Stock('Новый склад оргтехники')
pr1 = Printer(1, 'hp-1010', 'IT')
print(pr1)
my_stock.add_item(pr1)
my_stock.add_item(pr1)
print(pr1)
print(my_stock)
my_stock.pass_item(pr1, 'Бухгалтерия')
print(my_stock)
print(pr1)
my_stock.print_log()
sc1 = Scaner(2, 'samsung-xyz', 'HR', True)
print(sc1)
my_stock.add_item(sc1)
my_stock.print_log()
print(sc1)
mfu1 = MFU(3, 'Принер-сканер Vitek')
my_stock.pass_item(mfu1, 'Утиль')
my_stock.name = 'Удаленный склад'
print(sc1)
my_stock.print_log()
