

class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is: " + self.restaurant_name.title() + ".")
        print("Cuisine type is: " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, numCustomers):
        self.number_served = numCustomers

    def increment_number_served(self, perDay):
        self.number_served += perDay

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def print_flavors(self):
        for flavor in self.flavors:
            print(str(flavor))

iceCream = IceCreamStand("bucca di beppo", "italiano")
iceCream.print_flavors()