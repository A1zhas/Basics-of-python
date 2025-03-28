import requests
from bs4 import BeautifulSoup

def search_web(query):
    # Формируем URL для поиска
    search_url = f"https://www.google.com/search?q={query}"

    # Заголовки для подделки запроса (чтобы не заблокировали)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Печатаем информацию для отладки
    print(f"Поиск по запросу: {query}")
    print(f"URL запроса: {search_url}")

    # Отправляем запрос к Google
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Проверяем, что запрос успешен
        print(f"Запрос успешен, статусный код: {response.status_code}")
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе: {e}"

    # Разбираем страницу с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Печатаем полученный HTML для отладки
    print(soup.prettify())

    results = []

    # Находим все результаты поиска
    for item in soup.find_all('h3'):
        title = item.get_text()
        link = item.find_parent('a')['href']
        results.append({'title': title, 'link': link})

    return results
