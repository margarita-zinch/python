'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове.'''
str = input('введите строку из нескольких слов')
for idx, word in enumerate(str.split(' '), 1):
    print(f'{idx}:{word[:10]}')