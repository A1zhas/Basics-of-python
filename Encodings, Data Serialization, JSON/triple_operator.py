"""
Тернарный оператор
if - else, не должно быть elif
"""
import random

numbers = []

for i in range(30):
    numbers.append(random.randint(0, 100))

print(numbers)

# Проверить есть ли число 13 в нашем списке
if 13 in numbers:
    print('13 в нашем списке')
else:
    print('Нет несчастливого числа')


# Запись в 1 строку + меняется порядок выражений
# если условие верно <условие> если условение не верно
print('13 в нашем списке') if 13 in numbers else print('Нет несчастливого числа')


# Когда есть какая то переменная
result = None
if 4 in numbers:
    result = 'Есть китайское несчастливое число'
else:
    result = 'Все ок'

print('Результат выражения:', result)


result = 'Есть китайское несчастливое число' if 4 in numbers else 'Все ок'
print('Результат выражения:', result)


print('13 в нашем списке' if 13 in numbers else 'Нет несчастливого числа')
