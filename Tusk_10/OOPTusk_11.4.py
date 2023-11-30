from Basket import Basket
class User():

    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.basket = Basket()

user_1 = User("Nine", 9)
user_2 = User("13", 19234)
user_3 = User("Bob", 123)
user_1.__init__()