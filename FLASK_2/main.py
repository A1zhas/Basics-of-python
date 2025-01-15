from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html', title="Главная страница")

# Страница с контактами
@app.route('/contacts/')
def contacts():
    # Абсолютный путь до базы данных
    db_path = os.path.join(os.path.dirname(__file__), 'database', 'contacts.db')

    # Проверка существования папки и создание ее при необходимости
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))

    try:
        # Подключение к базе данных
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Получаем все контакты из базы данных
        cursor.execute("SELECT * FROM contacts")
        contacts_info = cursor.fetchall()

        # Закрываем соединение с базой данных
        conn.close()

    except sqlite3.OperationalError as e:
        # Обработка ошибок при подключении к базе данных
        return f"Ошибка подключения к базе данных: {e}"

    # Передаем список контактов в шаблон
    return render_template('contacts.html', title="Контакты", contacts=contacts_info)

# Страница с формой для добавления контакта
@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        # Путь до базы данных
        db_path = os.path.join(os.path.dirname(__file__), 'database', 'contacts.db')

        try:
            # Подключение к базе данных
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Вставляем данные в таблицу
            cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            conn.commit()

            # Закрываем соединение
            conn.close()

            # Перенаправляем обратно на страницу с контактами
            return redirect(url_for('contacts'))

        except sqlite3.OperationalError as e:
            return f"Ошибка при добавлении контакта: {e}"

    return render_template('add_contact.html', title="Добавить контакт")

# Страница с формой
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        query = request.form['query']
        # Заглушка: поиск цитат (можно подключить парсер)
        results = [{"text": f"Результат для {query}", "author": "Автор"}]
        return render_template('results.html', results=results)
    return render_template('form.html', title="Форма поиска")

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
