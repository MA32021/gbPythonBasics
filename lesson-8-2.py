# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class DivisionByZero(Exception):
    def __init__(self, err_msg=None):
        self.err_msg = err_msg if err_msg is not None else 'Возникло деление на ноль!'
        super().__init__(self.err_msg)


Finish = False
while not Finish:
    try:
        n1 = int(input('Введите делимое или не число для выхода: '))
        n2 = int(input('Введите делитель или не число для выхода: '))
        if n2 == 0:
            raise DivisionByZero('Делить на 0 нельзя!')
    except DivisionByZero as dbz:
        print(dbz)
    except ValueError:
        Finish = True
    else:
        print(f'Чaстное от деления {n1} на {n2} равно {n1 / n2}')
