class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} ")
        print(f"{self.cuisine_type} ")

    def open_restaurant(self):
        print(f"{self.restaurant_name} opened")

    def served_visitor(self):
        print(f"Served visitor: {self.number_served}")
    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_numbers_served(self, served):
        self.number_served += served


restaurant = Restaurant("Cheese", "Grecy")

restaurant.set_number_served(100)
restaurant.increment_numbers_served(29)
restaurant.served_visitor()

print(f"The most famous of restaurant: {restaurant.restaurant_name}.")
print(f"At this restaurant: {restaurant.cuisine_type} kitchen.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

