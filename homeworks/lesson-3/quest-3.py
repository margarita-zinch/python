'''Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
 сумму наибольших двух аргументов.'''
def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(a, b, c))
    return sum(numbers)
print(my_func(2, 6, 4))