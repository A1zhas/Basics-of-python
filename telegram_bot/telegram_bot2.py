import telebot
import time
import pprint
import os


TOKEN = '7582009929:AAHeEm9N4HPJ2IkkKkW5NncZCpGpP8HjmPE'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


#Обработка команд
@bot.message_handler(commands=['timer'])
def timer(message):
	for i in range(5):
		time.sleep(1)
		bot.send_message(message.chat.id, i+1)


#Команда с параметром
@bot.message_handler(commands=['say'])
def say(message):
	#Получить то что после команды
	text = ' '.join(message.text.split(' ')[1:])
	bot.reply_to(message, f'***{text.upper()}!***')


#Команда администратор
@bot.message_handler(commands=['admin'], func=lambda message: message.from_user.username == 'a1zhas_m')
def admin(message):
	print(message)
	info = os.name
	bot.reply_to(message, info)


@bot.message_handler(commands=['admin2'])
def admin2(message):
    if message.from_user.username == 'a1zhas_m':
        info = os.name
        bot.reply_to(message, info)
    else:
        bot.reply_to(message, 'Метод недоступен, нет прав')


@bot.message_handler(commands=['restart'])
def restart_server(message):
    # Выполняет команду для открытия Блокнота (для примера)
    # os.system('notepad')
    bot.reply_to(message, 'Ура! Блокнот открыт!')
		

@bot.message_handler(commands=['file'])
def get_file(message):
	#Передать какой-то файл который есть на диске
	#with open('text.txt', 'r', encoding='utf-8') as data:
		#bot.send_document(message.chat.id, data)
	with open('Porsche_911.jpg', 'rb') as data:
		bot.send_photo(message.chat.id, data)

@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'В тексте слово плохой')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
	FILE_ID ='CAACAgEAAxkBAAMsZ4S-Nke6hj9ECR9b8WhV2ycXCGkAAm0BAAJY7xAyYLcziV-Pl-Y2BA'
	bot.send_sticker(message.chat.id, FILE_ID)
	

bot.polling()
