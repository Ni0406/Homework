class Basket():

    def __init__(self):
        self.basket = []

    def add_item(self, item):
        self.basket.append(item)
        print(self.basket)

    def remove_item(self, item):
        if item in self.basket:
            self.basket.remove(item)
        print(self.basket)

    def get_item(self):
        return self.basket

    def make_purchases(self, ids):
        total_baskets = []
        for basket in self.basket:
            for id in ids:
                total_baskets.append(self.basket.pop(id))

        for total_basket in total_baskets:
            print(f"You buy {total_basket.title()}")

        raise print("Товаров с таким id в вашей корзине нет!")



