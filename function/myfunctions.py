def simple_separator():
    """
    Функция создает красивый разделитель из 10-и звездочек (**********)
    :return: строка **********
    """
    return '*' * 10  # Возвращаем строку из 10 звездочек


# Проверяем работу функции
print(simple_separator())  # **********
print()

def simple_separator(count=10):
    """
    Функция создает разделитель из звездочек, число которых можно регулировать параметром count.
    
    :param count: количество звездочек (по умолчанию 10)
    :return: строка из заданного количества звездочек
    """
    return '*' * count  # Возвращаем строку из заданного количества звездочек


# Пример использования
print(simple_separator())      # **********
print(simple_separator(5))     # *****
print(simple_separator(15))    # ***************
print()

def custom_separator(symbol='*', count=10):
    """
    Функция создает разделитель из любых символов с указанным количеством повторений.
    
    :param symbol: символ разделителя (по умолчанию '*')
    :param count: количество повторений символа
    :return: строка разделитель
    """
    return symbol * count  # Возвращаем строку, состоящую из символа, повторенного count раз


# Примеры использования
print(custom_separator('$', 3))     # $$$$
print(custom_separator('#', 4))     # ####
print(custom_separator('=', 5))     # =====
print()

def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    print('*' * 10)       # Печатаем 10 звездочек
    print('\nHello World!\n')  # Печатаем "Hello World!" с переносами строк
    print('#' * 10)       # Печатаем 10 символов '#'


# Пример использования
hello_world()
print()

def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате:
    **********

    Hello {who}!

    ##########
    
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print('*' * 10)              # Печатаем 10 звездочек
    print(f'\nHello {who}!\n')   # Печатаем "Hello {who}!" с переносами строк
    print('#' * 10)              # Печатаем 10 символов '#'
    

# Пример использования
hello_who()          # Приветствует World
hello_who('Aizhas')  # Приветствует Aizhas
hello_who('Alen')    # Приветствует Alen
print()

def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power.
    
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления
    """
    total = sum(args)  # Складываем все переданные аргументы
    return total ** power  # Возвращаем результат возведения в степень


# Примеры использования
print(pow_many(1, 1, 2) == (1 + 2) **1)                 # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == (2 + 3) **1)                 # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == (1 + 1) **2)                 # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == ( 2) **3)                       # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == (1 + 2 + 3 + 4) **2)   # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100
print()

def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в формате key --> value.
    
    key - имя параметра
    value - значение параметра
    
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print(f"{key} --> {value}")


# Пример использования
print_key_val(name="Aizhas", age=35, city="Almaty")
print('*' * 20)
print_key_val(animal='Cat', is_animal=True)
print()

def my_filter(iterable, function):
    """
    Функция фильтрует последовательность iterable и возвращает новую.
    Если function от элемента последовательности возвращает True, 
    то элемент входит в новую последовательность, иначе нет.
    
    :param iterable: входная последовательность
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    return [item for item in iterable if function(item)]  # Используем list comprehension для фильтрации



print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])      # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
