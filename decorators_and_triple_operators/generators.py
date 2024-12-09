from decorators import add_separators


def exception_handler(func):
    """
    Декоратор для обработки исключений.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None
    return wrapper


@exception_handler
@add_separators  # Сохраняем существующий декоратор
def manager_f():
    """
    Основная функция, демонстрирующая сообщение.
    """
    print('Создатель программы')
    # Пример использования тернарного оператора
    example = 'Тернарный оператор работает' if True else 'Не работает'
    print(example)
    # Пример генератора
    gen = (x**2 for x in range(5))
    print("Генератор:", ", ".join(map(str, gen)))


manager_f()
