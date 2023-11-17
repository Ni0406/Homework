import re


def replace_time_with_tbd(text):
    # Регулярное выражение для поиска времени в формате HH:MM:SS или HH:MM
    time_pattern = re.compile(r'\b(?:[01]\d|2[0-3]):(?:[0-5]\d)(?::(?:[0-5]\d))?\b')

    # Замена времени на "(TBD)"
    result = re.sub(time_pattern, '(TBD)', text)

    return result


# Пример использования
input_text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!"
output_text = replace_time_with_tbd(input_text)
print(output_text)
