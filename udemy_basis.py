# 1 форматирование строк

# name = 'Yauhen'
# age = 29
# name_and_age = ' My name is {0}. I\'m {1} years old.'.format(name, age)
# print(name_and_age)
# name_and_age = ' My name is {0}. I\'m {1} years old.'.format('Tom', age)
# print(name_and_age)
# name_and_age = ' My name is. I\'m years old.'.format('Tom', age)
# print(name_and_age)

# 2 форматирование, сколько знаков после запятой в числе при делении

# float_result = 253/24
# print(float_result)
# print('the result of devision is {0:1.4f}'.format(float_result))

#3 выравнивание по правому краю на уровне все числа + сколько чисел отобращать после запятой
# 0,1 ...это индексы,10 сколько знаков ходим выделить под каждое число

# print('''
#       {0:10.2f} {1:10.2f}
#       {2:10.2f} {3:10.2f}
#       {4:10.2f} {5:1.2f}'''.format(1.2222222,2.333333,3.44444,5.66666,5.33333,5556.44444))

#4 новый тип форматирование s strings в python3.6

# name = 'Yauhen'
# age = 29
# name_and_age = ' My name is {0}. I\'m {1} years old.'.format(name, age)
# print(name_and_age)
# name_and_age = f' My name {name} is. I\'m {age} years old.'
# print(name_and_age)

#5 Создайте таблицу из десятичных дробных чисел с дробной частью разного размера.
# В таблице должно быть 4 столбца и 2 строки. При помощи метода format()  выведите числа на экран так, чтобы всё число занимало 15 символов, 
# а дробная часть 4 символа

# print('''
#       {0:15.4f}{1:15.4f}{2:15.4f}{3:15.4f}'
#       {4:15.4f}{5:15.4f}{6:15.4f}{7:15.4f}'''.format(20.22222,21.22222,22.2222,23.2222,24.2222,25.2222,26.2222))



# list1 = [1,2.5,'no',222,634]

# another_list1 = list1[1:4]
# list1.append(another_list1)
# print(list1)

#6 Используйте цикл for для вычисления суммы всех чётных чисел в диапазоне от 10 до 30 (включая крайние значения). Выведите результат на печать


# sum_number = 0
# for number in range(10,31):
#     if number % 2 == 0:
#         sum_number += number
# print(sum_number)


# 7 Получите от пользователя число на вводе и используйте цикл for для вывода на экран текста 'Hello!' столько же раз

# word = input('Введите число ')

# for i in range(int(word)):
#     print('Hello')

# 8 соединить слова

# greetings = ['hello', 'hi', 'hey', 'hola']

# print(*greetings)


# 9 Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola']
# создайте новый список содержащий вторую букву из каждой строки исходного списка. Выведите новый список на печать.
# Решите задание двумя способами - при помощи List Comprehension и без него.

# greetings = ['hello', 'hi', 'hey', 'hola']
# new_greetings = []

# for greeting in greetings:
#    new_greetings.append(greeting[1])
# print(new_greetings)

greetings = ['hello', 'hi', 'hey', 'hola']
new_greetings = [greeting[1] for greeting in greetings]
print(new_greetings)


    
# 10 Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] создайте новый список содержащий нечетные числа исходного списка. 
# Выведите новый список на печать.
# Решите задание двумя способами - при помощи List Comprehension и без него.

# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# odd_digts = []

# for new_digts in digits:
#     if new_digts % 2 == 1:
#         odd_digts.append(new_digts)
# print(odd_digts)

# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_digits = [digit for digit in digits if digit % 2 == 1]
# print(odd_digits)

    



