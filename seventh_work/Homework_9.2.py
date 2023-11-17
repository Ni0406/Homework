import re


def count_words(text):
    # Используем регулярное выражение для извлечения слов с дефисами
    words = re.findall(r'[а-яА-Яa-zA-Z-]+', text)

    # Отфильтровываем слова, оставляя только те, которые состоят из букв
    words = [word for word in words if re.match(r'^[а-яА-Яa-zA-Z]+$', word)]

    return len(words)


# Пример использования
text = "Он --- серо-буро-малиновая редиска!! >>>:-> А не кот. www.kot.ru"
result = count_words(text)
print(result)
