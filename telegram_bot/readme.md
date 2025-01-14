📋 Описание работы бота
Telegram-бот "Парсер цитат" — это бот, который парсит сайт quotes.toscrape.com и отправляет пользователю цитаты с указанием авторов и тегов.

🛠 Доступные команды:
Команда	Описание
/start	Приветствие и информация о боте.
/help	Список доступных команд и описание их работы.
/parse	Запускает парсинг сайта и отправляет цитаты.
🚀 Как работает бот?
Бот отправляет GET-запрос на сайт quotes.toscrape.com.
Извлекает текст цитат, авторов и теги с помощью библиотеки BeautifulSoup.
Формирует сообщение и отправляет его в Telegram-чат.
Пример сообщения от бота:

markdown
Копировать код
📜 Цитата: “The best way to predict the future is to invent it.”
👤 Автор: Alan Kay
🏷️ Теги: future, prediction
--------------------------------------------------
📂 Как запустить бота?
Склонируй репозиторий:

bash
Копировать код
git clone https://github.com/Aizhas/Basics-of-python.git
Перейди в папку с ботом:

bash
Копировать код
cd Basics-of-python/telegram_bot
Установи зависимости:

bash
Копировать код
pip install requests beautifulsoup4 pyTelegramBotAPI
Замени токен в файле main_ya3_bot.py на свой токен:

python
Копировать код
TOKEN = 'ВАШ_ТОКЕН'
Запусти бота:
python main_ya3_bot.py