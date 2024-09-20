def main_menu():
    balance = 0
    purchase_history = []

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')
        
        if choice == '1':
            # Пополнение счета
            amount = float(input('Введите сумму для пополнения счета: '))
            balance += amount
            print(f'Счет пополнен на {amount}. Текущий баланс: {balance:.2f}')
        
        elif choice == '2':
            # Покупка
            purchase_amount = float(input('Введите сумму покупки: '))
            if purchase_amount > balance:
                print('Недостаточно средств на счете.')
            else:
                purchase_name = input('Введите название покупки: ')
                balance -= purchase_amount
                purchase_history.append((purchase_name, purchase_amount))
                print(f'Покупка "{purchase_name}" на сумму {purchase_amount:.2f} выполнена. Текущий баланс: {balance:.2f}')
        
        elif choice == '3':
            # История покупок
            if purchase_history:
                print('\nИстория покупок:')
                for name, amount in purchase_history:
                    print(f'{name}: {amount:.2f}')
            else:
                print('История покупок пуста.')
        
        elif choice == '4':
            # Выход
            print('Выход из программы.')
            break
        
        else:
            print('Неверный пункт меню. Попробуйте еще раз.')

# Запуск программы
main_menu()
