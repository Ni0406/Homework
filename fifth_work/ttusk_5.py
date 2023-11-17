# Информация о товарах и их наличии на складе
products = {
    "Товар 1": {"цена": 10, "осталось": 10},
    "Товар 2": {"цена": 20, "осталось": 0},
    "Товар 3": {"цена": 30, "осталось": 1}
}

# Корзина пользователя
cart = {}


# Функция вывода меню магазина
def show_menu():
    print("Меню магазина:")
    for product, info in products.items():
        print(f"{product} - Цена: ${info['цена']}, осталось: {info['осталось']}")


# Функция запроса выбора товара у пользователя
def get_user_choice():
    product_name = input("Выберите товар (введите название): ")
    return product_name


# Функция запроса количества товара у пользователя
def get_quantity():
    quantity = int(input("Введите количество единиц товара: "))
    return quantity


# Функция расчета общей стоимости товара
def calculate_total_price(product_name, quantity):
    product_info = products.get(product_name)
    if product_info and product_info['осталось'] >= quantity:
        total_price = product_info['цена'] * quantity
        return total_price
    else:
        print("К сожалению, данного товара недостаточно в наличии.")
        return None


# Функция размещения заказа
def place_order(product_name, quantity, total_price):
    if total_price:
        print("Ваш заказ размещен!")
        print(f"Общая стоимость заказа: ${total_price}")
        products[product_name]['осталось'] -= quantity
        cart[product_name] = quantity


# Функция проверки наличия товара на складе
def check_stock(product_name, quantity):
    product_info = products.get(product_name)
    if product_info and product_info['осталось'] >= quantity:
        return True
    else:
        print("К сожалению, данного товара недостаточно в наличии.")
        return False


# Функция поиска товара по названию в меню магазина
def search_item():
    search_query = input("Введите название товара для поиска: ")
    for product in products.keys():
        if search_query.lower() in product.lower():
            print(f"Найден товар: {product}")


# Функция добавления товара в корзину пользователя
def add_to_cart(product_name, quantity):
    cart[product_name] = quantity


# Функция отображения корзины пользователя
def show_cart():
    print("Ваша корзина:")
    for product, quantity in cart.items():
        print(f"{product} - Количество: {quantity}")


# Главная функция программы
def main():
    show_menu()
    product_name = get_user_choice()
    quantity = get_quantity()

    if check_stock(product_name, quantity):
        total_price = calculate_total_price(product_name, quantity)
        if total_price:
            place_order(product_name, quantity, total_price)
            show_cart()
        else:
            print("Заказ не может быть размещен из-за недостаточного количества товара.")

    # Пример использования функции поиска товара
    search_item()


# Вызов главной функции программы
if __name__ == "__main__":
    main()
