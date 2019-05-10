"""A class that can be used to represent a car"""

class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # an attribute that changes over time:  store the car's overall mileage

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make.title() + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print statement displaying the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        """add the given amount to the odometer reading"""
        self.odometer_reading += mileage



print("Cars suck gass.")