import requests
from bs4 import BeautifulSoup
import json
import telebot

# Твой Telegram-токен
TOKEN = '7582009929:AAHeEm9N4HPJ2IkkKkW5NncZCpGpP8HjmPE'

bot = telebot.TeleBot(TOKEN)

# Функция для парсинга цитат
def parse_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    quotes_list = []
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
        quotes_list.append({
            "text": text,
            "author": author,
            "tags": tags
        })
    return quotes_list

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для парсинга цитат. Введите команду /parse, чтобы начать.")

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Доступные команды:\n/start — начать работу\n/parse — получить цитаты")

# Команда /parse
@bot.message_handler(commands=['parse'])
def send_quotes(message):
    quotes = parse_quotes()
    for quote in quotes:
        bot.send_message(
            message.chat.id,
            f"📜 Цитата: {quote['text']}\n👤 Автор: {quote['author']}\n🏷️ Теги: {', '.join(quote['tags'])}\n\n{'-' * 50}"
        )
    bot.reply_to(message, "✅ Все цитаты отправлены!")

# Запуск бота
bot.polling()
