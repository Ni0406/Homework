class Category():

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_item(self, item):
        self.goods.append(item)
        print(self.goods)

    def remove_item(self, item):
        if item in self.goods:
            self.goods.remove(item)
        print(self.goods)

    def get_item(self, index):
        if 0 <= index < len(self.goods):
            return self.goods[index]
        else:
            return None


category1 = Category("Clothing")
category2 = Category("Electronics")

category1.add_item("T-shirt")
category1.add_item("Jeans")
category1.add_item("Jacket")

category2.add_item("Smartphone")
category2.add_item("Laptop")
category2.add_item("Headphones")
