# Multiple Inheritance

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are general means of transportation"
    
    @property
    def model(self):
        return self.__model
    

class ElecticCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

class Battery:
    def batter_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class Electric_car(Battery, Engine, Car):
    pass


my_new_tesla = Electric_car("Tesla", "Model S")

print(my_new_tesla.engine_info())
print(my_new_tesla.batter_info())
print(my_new_tesla.get_brand())
print(my_new_tesla.model)
print(my_new_tesla.full_name())
print(my_new_tesla.fuel_type())


# my_tesla = ElecticCar("Tesla", "Model S", "85kWh") #1
# my_car = Car("Toyato", "Corolla") #2
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElecticCar))
# my_car.model = "city"  // not change model because of @property
# print(my_car.model)
# # print(my_car.general_description())
# print(Car.general_description())
