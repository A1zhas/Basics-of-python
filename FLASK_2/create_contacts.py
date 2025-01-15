import sqlite3
import os

# Путь к базе данных
db_path = os.path.join(os.path.dirname(__file__), 'database', 'contacts.db')

def insert_sample_data():
    # Подключаемся к базе данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Пример данных для вставки
    contacts = [
        ("Иван Иванов", "ivan@example.com", "+7 777 123 4567"),
        ("Мария Петрова", "maria@example.com", "+7 777 234 5678"),
        ("Петр Сидоров", "peter@example.com", "+7 777 345 6789")
    ]

    # Вставляем данные
    cursor.executemany('INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)', contacts)

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()

# Вставка данных в базу
insert_sample_data()
