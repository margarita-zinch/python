'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''
from sys import argv

hour, rate, bonus = argv
try:
    hour = float(hour)
    rate = float(rate)
    bonus = float(bonus)
    result = hour * rate + bonus
    print(result)
except ValueError:
    print('Ошибка ввода')

