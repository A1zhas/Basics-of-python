"""
Генераторы списков!
Функции генераторы
тип генератор
генераторные выражение - генераторы списков
простая запись цикла for
"""
import random

numbers = [1, 4, 2, 6, 7, 10, 100]

# найти числа больше 5 и меншья 50
# просто цикл for
result = []
for number in numbers:
    if number > 5 and number < 50:
        result.append(number)

print(result)

# filter
result = filter(lambda number: number > 5 and number < 50, numbers)

print(list(result))

# генератор списка
# [элемент <цикл for> if <условие>]

result = [number for number in numbers if number > 5 and number < 50]
print(result)

names = ['leo', 'max', 'kate', 'mag']

# Создать список из имен каждое имя большими буквами
names_upper = [name.upper() for name in names]

print(names_upper)

# Найти имена на букву m
names_m = [name for name in names if name[0] == 'm']
print(names_m)

# names_m = [name for name in names if 'm' in name]
# print(names_m)
#
# names_m = [name for name in names if 'm' in names]
# print(names_m)

#
names_m = [name for name in names if name.lower().startswith('m')]
print(names_m)

numbers = [1, 4, 2, 6, 7, 10, 100]

# если числа больше 5 то пишем в список 1, а если меньше то пишем в список 0
# [0, 0, 0, 1, 1, 1, 1]

# Комбинация тернарного оператора и генератора
result = [1 if number > 5 else 0 for number in numbers]

print(result)

# Есть генераторы множеств и генераторы словарей
# set - создать неповторяющиеся случайные числа из 100 штук

result = set([random.randint(1, 100) for i in range(100)])
print(result)

# Генератор сета
result = {random.randint(1, 100) for i in range(100)}
print(result)
print(type(result))

# Генератор словаря
result = {i: i ** 2 for i in range(1, 10)}

print(result)

names = ['leo', 'max', 'kate', 'mag', 'mr.bin']

# ключе - имя человека, значение будет длина его имени
result = {name: len(name) for name in names}

print(result)