# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

try:
    revenue = int(input("Введите значение выручки: "))
    cost = int(input("Введите значение издержек: "))
    profit = revenue - cost
    profitability = 0
    ppe = 0
    if profit > 0:
        result = "прибылью"

        # 6. Если фирма отработала с прибылью,
        # вычислите рентабельность выручки.
        # Это отношение прибыли к выручке.
        # Далее запросите численность сотрудников фирмы
        # и определите прибыль фирмы в расчёте на одного сотрудника.

        profitability = profit / revenue
        headcount = int(input("Введите численность сотрудников: "))
        ppe = profit / headcount
    elif profit == 0:
        result = "нулевым результатом"
    else:
        result = "убытком"
    print(f'Фирма работает с {result}')
    if profit > 0:
        print("Рентабельность равна: {:.5f}".format(profitability))
        print("Прибыль на одного сотрудника составляет: {:.5f}".format(ppe))
except:
    print("Введено неверное значение. Попробуйте еще раз")
