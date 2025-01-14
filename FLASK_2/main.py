from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html', title="Главная страница")

# Страница с контактами
@app.route('/contacts/')
def contacts():
    contacts_info = {
        "email": "support@example.com",
        "phone": "+7 777 123 4567"
    }
    return render_template('contacts.html', title="Контакты", contacts=contacts_info)


# Страница с формой
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        query = request.form['query']
        # Заглушка: поиск цитат (здесь можно подключить парсер)
        results = [{"text": f"Результат для {query}", "author": "Автор"}]
        return render_template('results.html', results=results)
    return render_template('form.html', title="Форма поиска")

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
