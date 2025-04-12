class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move")

class car(vehicle):
    pass


class boat(vehicle):
    def move(self):
        print('Sail')

class plane(vehicle):
    def move(self):
        print("Fly")

car1 = car("Ford", "Mustang")
boat1 = boat("Ibiza", 'touring 20')
plane1 = plane("Boeing", "745")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()