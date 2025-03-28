from flask import Flask, render_template, request
import os


app = Flask(__name__)


@app.route('/')
def index():
    main_data = {
        'a': 'A',
        'b': 'B',
        'c': 'C'
    }

    context = {
        'name': 'Leo',
        'age': 99
    }
    
    return render_template('index.html', main_data=main_data, **context)
    # return render_template('index.html', main_data=main_data, name='Leo', age=99)

@app.route('/contacts/')
def contacts():
    # Где то взяли данные
    developer_name = 'Leo'
    # Контекст name=developer_name - те данные, которые мы передаем из view в шаблон
    return render_template('contacts.html', name=developer_name, creation_date='14.01.2025')
    # context = {'name': developer_name}
    # Словарь контекста
    # return render_template('contacts.html', props=context)

@app.route('/results/')
def results():
    data = ['python', 'js', 'java', 'sql', 'c#']
    #data = []
    return render_template('results.html', data=data)


@app.route('/run/', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        text = request.form.get('input_text', '').strip()
        if text:
            with open('main.txt', 'w') as f:
                f.write(f'{text}\n')
            return render_template('good.html')
        else:
            return render_template('form.html', text='', error='Введите текст!')

    if os.path.exists('main.txt'):
        with open('main.txt', 'r') as f:
            text = f.read()
    else:
        text = ''
    return render_template('form.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)