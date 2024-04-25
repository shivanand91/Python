# class variable

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElecticCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

ElecticCar("Tesla", "Model S", "85kWh") #1
Car("Toyato", "Corolla") #2


print(Car.total_car)
print(ElecticCar.total_car)





# print(my_car.fuel_type())
# print(my_tesla.fuel_type())
# print(my_tesla.get_brand())
# print(my_tesla.full_name(), my_tesla.battery_size)
# print(my_car.__brand)
# print(my_car.model)
# print(my_car.full_name())