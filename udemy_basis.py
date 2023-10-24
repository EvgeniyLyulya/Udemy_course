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

#4 новый тип форматирование s strings

name = 'Yauhen'
age = 29
name_and_age = ' My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = f' My name {name} is. I\'m {age} years old.'
print(name_and_age)
