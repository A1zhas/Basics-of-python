import requests
from bs4 import BeautifulSoup
import json

# URL для парсинга
url = "https://quotes.toscrape.com/"

# Отправляем GET-запрос
response = requests.get(url)
response.raise_for_status()

# Создаем объект BeautifulSoup для парсинга
soup = BeautifulSoup(response.text, "html.parser")

# Находим все цитаты на странице
quotes = soup.find_all("div", class_="quote")

# Создаем списки для хранения данных
quotes_list = []

# Проходим по каждой цитате и собираем данные
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

    # Вывод в консоль
    print(f"Цитата: {text}")
    print(f"Автор: {author}")
    print(f"Теги: {', '.join(tags)}")
    print("-" * 50)

    # Добавляем данные в список
    quotes_list.append({
        "text": text,
        "author": author,
        "tags": tags
    })

# Сохранение в quotes.txt
with open("quotes.txt", "w", encoding="utf-8") as txt_file:
    for quote in quotes_list:
        txt_file.write(f"Цитата: {quote['text']}\n")
        txt_file.write(f"Автор: {quote['author']}\n")
        txt_file.write(f"Теги: {', '.join(quote['tags'])}\n")
        txt_file.write("-" * 50 + "\n")

# Сохранение в quotes.json
with open("quotes.json", "w", encoding="utf-8") as json_file:
    json.dump(quotes_list, json_file, ensure_ascii=False, indent=4)

print("Данные сохранены в quotes.txt и quotes.json")
