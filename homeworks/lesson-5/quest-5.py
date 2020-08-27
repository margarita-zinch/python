'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''
import os
file_path = os.path.join(os.path.dirname(__file__), 'quest5.txt')
to_file_numbers = [random.randint(1, 200) for _  in range(random.randit(10, 250))]
print(sum(to_file_numbers))
with open(file_path, 'w', encoding='UTF') as file:
    numbers = map(int, file.read().split('  '))
print(sum(numbers))
assert sum(to_file_numbers) ==sum(numbers), 'Сработал ASSERT'
