import os

def list_directory_content(path='.'):
    """Функция для получения содержимого директории."""
    files = []
    dirs = []
    
    # Получаем все файлы и директории
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
        elif os.path.isdir(os.path.join(path, item)):
            dirs.append(item)
    
    # Возвращаем отсортированные списки файлов и папок
    return sorted(files), sorted(dirs)

def save_directory_content(path='.', filename='listdir.txt'):
    """Функция для сохранения содержимого рабочей директории в файл."""
    # Получаем файлы и папки в директории
    files, dirs = list_directory_content(path)
    
    # Открытие файла для записи, перезаписываем его, если он существует
    with open(filename, 'w', encoding='utf-8') as f:
        # Записываем файлы в формате: files: file1.txt, file2.txt
        f.write(f'files: {", ".join(files)}\n')
        # Записываем папки в формате: dirs: folder1, folder2
        f.write(f'dirs: {", ".join(dirs)}\n')

# Основное меню программы
while True:
    print("Меню:")
    print("1. Просмотр содержимого рабочей директории")
    print("2. Сохранить содержимое рабочей директории в файл")
    print("3. Выход")
    
    choice = input("Введите номер: ")
    
    if choice == '1':
        # Просмотр содержимого директории
        files, dirs = list_directory_content()
        print("Файлы:", files)
        print("Папки:", dirs)
    elif choice == '2':
        # Сохранение содержимого директории в файл
        save_directory_content()
        print("Содержимое рабочей директории сохранено в файл listdir.txt.")
    elif choice == '3':
        break
    else:
        print("Неверный выбор, попробуйте снова.")