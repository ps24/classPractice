from car import Car
from electric_car import ElectricCar

my_beetle = Car('beetle', 'volkswagen', 2000)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())