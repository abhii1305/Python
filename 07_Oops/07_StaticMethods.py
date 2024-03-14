class Car:
    total_car=0

    def __init__(self,brand, model):
        self.__brand=brand
        self.model=model

        Car.total_car +=1

    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

    @staticmethod
    def general_description():
        return "Cars are Means of Transport"
    
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Elecrtic Charge"

# my_Tesla=ElectricCar("Tesla","Model S", "85kWh")
# # print(my_Tesla.__brand)
# print(my_Tesla.fuel_type())


my_car = Car("Tata","Safari")
Car("Tata","Nexon")
# safariThree = Car("Tata","Nexon")

print(my_car.fuel_type())
print(Car.general_description())

# print(safari.total_car)
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())