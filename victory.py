# Создаем словарь с именами и годами рождения известных людей
famous = {
    "Эйнштейн": 1879,
    "Моцарт": 1756,
    "Шекспир": 1564,
    "Кьюри": 1867,
    "Ганди": 1869
}

# Инициализируем переменные для подсчета результатов
correct_answer = 0
mistakes = 0

# Проходимся по словарю и задаем вопросы
for human, year in famous.items():
    answer = input(f"Введите год рождения {human}: ")
    try:
        answer = int(answer)
        if answer == year:
            correct_answer += 1
        else:
            mistakes += 1
    except ValueError:
        mistakes += 1

# Считаем проценты
answ = len(famous)
prc_correct = (correct_answer / answ) * 100
prc_mistakes = (mistakes / answ) * 100

# Выводим результаты
print(f"Количество правильных ответов: {correct_answer}")
print(f"Количество ошибок: {mistakes}")
print(f"Процент правильных ответов: {prc_correct}%")
print(f"Процент ошибок: {prc_mistakes}%")
