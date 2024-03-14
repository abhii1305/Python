# basic class n object
# Create a Car class with attributes like brand and model.Then create an instance of the class
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model


my_car = Car("Toyotta","Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car= Car("Tata", "Safari")
print(my_new_car.model)