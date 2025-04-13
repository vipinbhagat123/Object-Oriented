# Encapsulation in Python
# Encapsulation is a concept of wrapping data and methods in a single unit. It restricts direct access to some of the object's components.
# Modify the car class to encapsulate the brand attribute, making it private. Add a getter method to access the brand attribute.

class car:
    def __init__(self, brand, model):
        self.__brand = brand        # __ it is private variable
        self.model = model
    
    def get_brand(self):
        return self.__brand         # Accessing private variable using getter method

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def full_name(self):
        return f"{self.brand} {self.model} with battery size {self.battery_size}"

k=ElectricCar("Tesla", "Model S", "100kWh")
#print(k.brand) # This will give an error because brand is private
print(k.get_brand())    # Accessing private variable using getter method