# Class Variable
# Problem : Add a class varibale to car that keeps track of the number of cars created.

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car +=1
    
    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Disel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def full_name(self):
        return f"{self.brand} {self.model} with battery size {self.battery_size}"
    
    def fuel_type(self):
        return "Electric Charge"
k=ElectricCar("Tesla", "Model S", "100kWh")
l=Car("Toyota", "Corolla")
print(l.brand) 
print(l.model)
print(l.fuel_type())

print(k.brand)
print(k.model)
print(k.battery_size)
print(k.full_name())
print(k.fuel_type())
print(Car.total_car)