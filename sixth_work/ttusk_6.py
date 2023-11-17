kurs = {
    "Программирование": {
        "Средний бал": 261,
        "Количество мест": 110,
    },
    "Кулинария": {
        "Средний бал": 288,
        "Количество мест": 20,
    },
    "Ораторское Искусство": {
        "Средний бал": 225,
        "Количество мест": 35,
    }
}

def check_available(direction, total_points):
    if direction in kurs and total_points >= kurs[direction]["Средний бал"]:
        if kurs[direction]["Количество мест"] > 0:
            kurs[direction]["Количество мест"] -= 1
            return f"Поздравляем, вы прошли на направление {direction}!"
        else:
            return "Извините, места на данном направлении уже закончились."
    else:
        return "Извините, вам не хватило баллов для данного направления."

def info_student(first_name, last_name, name_group, total_points, thirst_name=None):
    if thirst_name:
        full_name = f"{last_name} {first_name} {thirst_name}"
    else:
        full_name = f"{last_name} {first_name}"
    direction = name_group
    return f"{full_name}\ndirection: {direction}\ntotal_bal: {total_points}"

def main():
    while True:
        first_name = input("Введите свое имя (или 'q' для завершения): ")
        if first_name == 'q':
            break
        last_name = input("Введите свою фамилию (или 'q' для завершения): ")
        if last_name == 'q':
            break
        thirst_name = input("Введите свое отчество (или 'q' для завершения): ")
        if thirst_name == 'q':
            break

        name_group = input("Введите желаемое направление (или 'q' для завершения): ")
        if name_group == 'q':
            break

        total_points = int(input("Введите сумму ваших баллов: "))

        info_person = info_student(first_name, last_name, name_group, total_points, thirst_name)
        print(info_person)

        result = check_available(name_group, total_points)
        print(result)

if __name__ == "__main__":
    main()
