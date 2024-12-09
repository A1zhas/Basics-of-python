import os

FILE_NAME_BALANCE = 'bank_account.txt'
FILE_NAME_ORDERS = 'orders.txt'

# Загрузка текущего баланса
def load_balance():
    if os.path.exists(FILE_NAME_BALANCE):
        with open(FILE_NAME_BALANCE, 'r') as f:
            balance = f.read().strip()
            return float(balance) if balance else 0.0
    return 0.0  # Если файл не существует, возвращаем 0.0

# Сохранение текущего баланса
def save_balance(balance):
    with open(FILE_NAME_BALANCE, 'w') as f:
        f.write(str(balance))

# Загрузка истории покупок
def load_orders():
    if os.path.exists(FILE_NAME_ORDERS):
        with open(FILE_NAME_ORDERS, 'r') as f:
            orders = [order.strip() for order in f.readlines()]
            return orders
    return []  # Если файла нет, возвращаем пустой список

# Сохранение истории покупок
def save_orders(orders):
    with open(FILE_NAME_ORDERS, 'w') as f:
        for order in orders:
            f.write(f'{order}\n')

# Основная программа
balance = load_balance()  # Загружаем баланс при старте
orders = load_orders()  # Загружаем историю покупок при старте

while True:
    print("\nМеню:")
    print("1. Добавить покупку")
    print("2. История покупок")
    print("3. Показать баланс")
    print("4. Пополнить баланс")
    print("5. Выход")
    
    choice = input('Введите номер: ')
    
    if choice == '1':
        name = input('Введите название покупки: ')
        orders.append(name)
        print(f'Покупка "{name}" добавлена.')
    elif choice == '2':
        print("История покупок:")
        if orders:
            for order in orders:
                print(order)
        else:
            print("История покупок пуста.")
    elif choice == '3':
        print(f"Текущий баланс: {balance:.2f}")
    elif choice == '4':
        amount = float(input('Введите сумму для пополнения: '))
        if amount > 0:
            balance += amount
            print(f"Баланс успешно пополнен на {amount:.2f} единиц.")
        else:
            print("Сумма пополнения должна быть больше нуля.")
    elif choice == '5':
        # Сохраняем данные перед выходом
        save_balance(balance)
        save_orders(orders)
        print('Данные сохранены. Выход из программы.')
        break
    else:
        print('Неправильный ввод, попробуйте снова.')
