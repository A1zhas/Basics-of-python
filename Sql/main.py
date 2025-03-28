# hh
# Название, регион, ключевые скилы
# python developer, Москва, (python, sql)
# Java developer, Питер, (java spring)
# ruby, Москва, (python, ruby)

# Реляционная база
# таблицв, связи

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('c:/Users/Aizhas/Desktop/python/Basics-of-python/Sql/hh.db')

cursor = conn.cursor()

# Если запрос ничего не возвращает то делаем execute
# cursor.execute('insert into region (name) VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35,14)')

cursor.execute('SELECT * from region')

result = cursor.fetchall()
print(result)

for item in result:
    print(item)
    print(type(item))


cursor.execute('SELECT * from region where name=?', ('Москва',))

print(cursor.fetchall())

# Если запрос ничего не возвращает то делаем execute
cursor.execute('INSERT INTO vacancykey_skills (vacancy_id, key_skiils_id) VALUES (?, ?)', (1, 5))

cursor.execute('SELECT * FROM vacancykey_skills')

print(cursor.fetchall())

# Вывести в нормальном виде таблицу скилы + вакансии

query = '''select vk.id, v.name, k.name, r.name from vacancy v, 
key_skills k, vacancykey_skills vk, region r where vk.vacancy_id = v.id and 
vk.key_skiils_id = k.id and v.region_id = r.id'''

cursor.execute(query)

print(cursor.fetchall())
