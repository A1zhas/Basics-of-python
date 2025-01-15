import sqlite3

conn = sqlite3.connect('c:/Users/Aizhas/Desktop/python/Basics-of-python/Sql/hh.db')
cursor = conn.cursor()

# Проверка структуры таблицы vacancykey_skills
cursor.execute('PRAGMA table_info(vacancykey_skills);')
columns = cursor.fetchall()

# Вывод структуры таблицы
print("Структура таблицы vacancykey_skills:")
for column in columns:
    print(column)

conn.close()
