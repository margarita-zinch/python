'''3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''
while True:
    month = input('введите целое число от 1 до 12')
    if month.isdigit():
        month: int = int(month),
        break
        print('ошибка ввода, это не число')

seasons = {'winter',
           'spring',
           'summer',
           'autumn',
}

month = 12
seasons_idx = month // 3 % 4
print (seasons_idx)
