class Product():
    def __init__(self, name, id, price, rating, quantity_available_product):
        self.name = name
        self.__id = id
        self.price = price
        self.rating = rating
        self.quantity_available_product = quantity_available_product
        self.basket = []

    def __str__(self):
        return print(f"Name {self.name.title()}, Id: {self.__id}, Price: {self.price}$, Rating: {self.rating}, Available: {self.quantity_available_product}")

    def add_stock(self, name_product):
        self.basket.append(self.name)
        print(self.basket)

    def remove_stock(self, quit):
        if quit == "q":
            self.basket.remove(self.name)
        print(self.basket)

    def update_rating(self, rate):
        if rate <= 100:
            self.rating = rate

    def update_price(self, price):
        self.price = price
        print(self.price)

product_1 = Product("Potato", "00001",  10, 100 , 1_000_000)
product_1.__str__()