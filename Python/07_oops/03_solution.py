# Inheritance
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
class ElecticCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElecticCar("Tesla", "Model S", "85kWh")
my_car = Car("Toyato", "Corolla")

print(my_tesla.full_name(), my_tesla.battery_size)

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())