import sqlite3
import os

def create_database():
    # Путь до базы данных
    database_folder = os.path.join(os.path.dirname(__file__), 'database')
    
    # Создаём папку, если она не существует
    if not os.path.exists(database_folder):
        os.makedirs(database_folder)

    # Путь до файла базы данных
    db_path = os.path.join(database_folder, 'contacts.db')

    # Подключаемся к базе данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создаём таблицу
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    # Закрываем соединение с базой данных
    conn.commit()
    conn.close()

# Вызываем функцию для создания базы данных
create_database()
