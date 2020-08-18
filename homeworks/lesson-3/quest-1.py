'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def divis(number: float, number2: float) -> float:
    try:
        return number1 / number2
    except ZeroDivisionError:
        return '!!!На ноль делить нельзя!!!'
number1 = (int(input("Введите первое число: ")))
number2 = (int(input("Введите второе число: ")))
print(divis(number1, number2))

