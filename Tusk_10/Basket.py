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

    def get_item(self, index):
        if 0 <= index < len(self.basket):
            return self.basket[index]
        else:
            return None

    def make_purchases(self, id):
        if id in self.basket:
            pep = self.basket.pop(id)
            print(f"You buy {pep.title()}")

        raise print("Товара с таким id в вашей корзине нет!")


