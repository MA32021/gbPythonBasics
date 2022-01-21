# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("Введите целое положительное число: ")
done = False
maxDigit = 0
position = 10
try:
    number = int(number)
    if number > 0:
        while not done:
            if maxDigit < number % position:
                maxDigit = number % position
            if position > number:
                done = True
            else:
                number = number // position
    else:
        print("Введенное число <= 0. Попробуйте еще раз")
except:
    print("Вы ввели не число. Попробуйте еще раз")
finally:
    print(f'Самая большая цифра в числе равна {maxDigit}')
