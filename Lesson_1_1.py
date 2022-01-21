# 1. Поработайте с переменными, создайте несколько,
# выведите на экран. Запросите у пользователя некоторые числа
# и строки и сохраните в переменные, затем выведите на экран.

varInt = 12
print(varInt)

varFloat = 1.0
print(varFloat)

varNone = None
print(varNone)

varString = "строка"
print(varString)

varList = [1, 'два', 3, 4, "пять"]
print(varList)

varDict = (1, 1, 1, 0, 3, 5)
print(varDict)

varTuple = {1: "один", 2: "два", 3: "три"}
print(varTuple)

varLogical = True
print(varLogical)

login = input("Введите логин: ")
pin = int(input("Введите пин-код: "))

print(f'Введена кобминация логина "{login}" и пин-кода {pin}')
