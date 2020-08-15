'''2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().'''


numbers = input('введите числа через запятую')
number_list = numbers.split(',')
idx = 0
len_idx = len(number_list) - 1
while idx < len_idx:
    number_list[idx], number_list[idx + 1] = number_list[idx + 1], number_list[idx]
    idx += 2
print(number_list)
