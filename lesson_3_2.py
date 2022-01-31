# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def display_user_info(name='', surname='', yob=0, residence='', email='', phone=''):
    """Функция вывода данных о пользователе

    :param name: имя
    :param surname: фамилия
    :param yob: год рождения
    :param residence: город проживания
    :param email: email
    :param phone: телефон
    :return: None
    """
    print(f'Пользователь {name} {surname},\n{yob} года рождения,\nпроживает в {residence},\nтелефон: {phone},\nemail: {email}')

display_user_info(name='John', surname='Smith', residence='Manchester', yob=1980, email='jsmith@nowhere.net', phone='222-33-44')
