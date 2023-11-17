import re


def check_license_plate(plate):
    private_car_pattern = re.compile(r'^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')
    taxi_pattern = re.compile(r'^[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}$')

    plates = plate.split()  # Разделяем строку на список номеров
    results = []

    for plate in plates:
        if private_car_pattern.match(plate):
            results.append('Частный')
        elif taxi_pattern.match(plate):
            results.append('Такси')
        else:
            results.append('Не номер')

    return results


# Пример использования для строки с несколькими номерами
license_plate_string = "С227НА777 КУ22777 Т22В7477 М227К19У9"
results = check_license_plate(license_plate_string)

# Выводим результаты
for i, result in enumerate(results, start=1):
    print(f"Номер {i}: {result}")
