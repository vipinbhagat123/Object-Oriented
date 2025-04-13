# Inheritance
# problem : Create an Electriccar class that inherits from the car class and has an additional attribute batterY_size.

class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectericCar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def full_name(self):
        return f"{self.brand} {self.model} with battery size {self.battery_size}"


k=ElectericCar("Tesla", "Model S", "100kWh")
print(k.brand)
print(k.model)  
print(k.battery_size)
print(k.full_name())