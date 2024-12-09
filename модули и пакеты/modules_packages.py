import os
import shutil
import platform

def create_directory():
    name = input('Введите имя папки для создания: ')
    os.makedirs(name, exist_ok=True)
    print(f'Папка "{name}" успешно создана.')

def delete_item():
    name = input('Введите имя файла или папки для удаления: ')
    if os.path.exists(name):
        if os.path.isfile(name):
            os.remove(name)
            print(f'Файл "{name}" успешно удален.')
        elif os.path.isdir(name):
            shutil.rmtree(name)
            print(f'Папка "{name}" успешно удалена.')
    else:
        print('Файл или папка не найдены.')

def copy_item():
    source = input('Введите имя файла или папки для копирования: ')
    destination = input('Введите имя папки назначения: ')
    if os.path.exists(source):
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print(f'Файл "{source}" успешно скопирован в "{destination}".')
        elif os.path.isdir(source):
            shutil.copytree(source, os.path.join(destination, os.path.basename(source)))
            print(f'Папка "{source}" успешно скопирована в "{destination}".')
    else:
        print('Файл или папка не найдены.')

def list_contents():
    print('\nСодержимое рабочей директории:')
    for item in os.listdir():
        print(item)

def list_folders():
    print('\nПапки в текущей директории:')
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)

def list_files():
    print('\nФайлы в текущей директории:')
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)

def os_info():
    print(f'\nИнформация об ОС: {platform.system()} {platform.release()}')

def creator_info():
    print('\nСоздатель программы: Ваше имя')

def quiz():
    print('\nВикторина:')
    question = "Сколько будет 2 + 2? "
    answer = input(question)
    if answer == '4':
        print("Верно!")
    else:
        print("Неверно!")

def bank_account():
    print('\nМой банковский счет: 0.00')

def change_directory():
    new_dir = input('Введите путь к новой рабочей директории: ')
    try:
        os.chdir(new_dir)
        print(f'Рабочая директория изменена на: {os.getcwd()}')
    except FileNotFoundError:
        print('Директория не найдена.')

def main_menu():
    while True:
        print('\n--- Консольный файловый менеджер ---')
        print('1. Создать папку')
        print('2. Удалить (файл/папку)')
        print('3. Копировать (файл/папку)')
        print('4. Просмотр содержимого рабочей директории')
        print('5. Посмотреть только папки')
        print('6. Посмотреть только файлы')
        print('7. Просмотр информации об операционной системе')
        print('8. Создатель программы')
        print('9. Играть в викторину')
        print('10. Мой банковский счет')
        print('11. Смена рабочей директории')
        print('12. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            create_directory()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            copy_item()
        elif choice == '4':
            list_contents()
        elif choice == '5':
            list_folders()
        elif choice == '6':
            list_files()
        elif choice == '7':
            os_info()
        elif choice == '8':
            creator_info()
        elif choice == '9':
            quiz()
        elif choice == '10':
            bank_account()
        elif choice == '11':
            change_directory()
        elif choice == '12':
            print('Выход из программы.')
            break
        else:
            print('Неверный пункт меню. Попробуйте снова.')

# Запуск программы
if __name__ == "__main__":
    main_menu()
