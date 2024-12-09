import unittest
import os
from io import StringIO
import sys

# Предположим, что ваши функции находятся в файле `file_manager.py`
from file_manager import list_directory_content, save_directory_content


class TestDirectoryFunctions(unittest.TestCase):

    def setUp(self):
        # Создание временной тестовой директории
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)

        # Создание временных файлов и папок
        self.test_file1 = os.path.join(self.test_dir, 'file1.txt')
        self.test_file2 = os.path.join(self.test_dir, 'file2.txt')
        self.test_subdir = os.path.join(self.test_dir, 'subdir')

        with open(self.test_file1, 'w') as f:
            f.write('Hello World')
        with open(self.test_file2, 'w') as f:
            f.write('Hello Python')
        os.makedirs(self.test_subdir)

    def tearDown(self):
        # Удаление тестовой директории и файлов
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_list_directory_content(self):
        # Проверяем, что функция корректно извлекает файлы и папки
        files, dirs = list_directory_content(self.test_dir)
        self.assertIn('file1.txt', files)
        self.assertIn('file2.txt', files)
        self.assertIn('subdir', dirs)

    def test_save_directory_content(self):
        # Проверяем, что содержимое директории сохраняется в файл
        save_directory_content(self.test_dir, 'listdir.txt')

        # Проверяем содержимое файла
        with open('listdir.txt', 'r') as f:
            content = f.read()
            self.assertIn('files: file1.txt, file2.txt', content)
            self.assertIn('dirs: subdir', content)

if __name__ == '__main__':
    unittest.main()
