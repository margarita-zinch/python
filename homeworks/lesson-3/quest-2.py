'''Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год
рождения, город проживания, email, телефон.Функция должна принимать параметры как именованные аргументы.Реализовать
вывод данных о пользователе одной строкой.'''
def data(name, surname, year, city, email, tel):
    name = name.title()
    surname = surname.title()
    year = int(year)
    city = city.title()
    email = email.title()
    tel = int(tel)
    return f" имя {name}, фамилия {surname}, год рождения {year},  проживает в городе {city},  email {email}, телефон {tel}"

