import unittest
from unittest.mock import patch
from io import StringIO
from file_manager_8 import manager_f, exception_handler  # Импортируйте свою функцию

class TestManagerFunction(unittest.TestCase):
    def test_manager_f_output(self):
        """
        Тестирует вывод функции manager_f с декораторами.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manager_f()
            output = mock_stdout.getvalue().strip()
            expected_output = (
                "--------------------\n"
                "Создатель программы\n"
                "Тернарный оператор работает\n"
                "Генератор: 0, 1, 4, 9, 16\n"
                "--------------------"
            )
            self.assertEqual(output, expected_output)

    def test_exception_handler(self):
        """
        Проверяет, обрабатываются ли исключения.
        """
        @exception_handler
        def faulty_function():
            raise ValueError("Ошибка!")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = faulty_function()
            output = mock_stdout.getvalue().strip()
            self.assertIn("Произошла ошибка: Ошибка!", output)
            self.assertIsNone(result)  # Убедимся, что вернулось None


if __name__ == "__main__":
    unittest.main()
