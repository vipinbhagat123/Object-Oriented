# Self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.

class Dog:
    species = 'Canine'   # class attribute

    def __init__(self, name, age):
        self.name = name    # Instance Attribute
        self.age = age      # Instance Attribute

dog1 = Dog("Budddy", 3) # create an instance of dog
dog2 = Dog("Max", 5)   # create another instance of dog

print(dog1.name, dog1.age, dog1.species)    # Access instance and class attrubtes
print(dog2.name, dog2.age, dog2.species)    # Access instance and class attrubtes
print(dog1.species)    # Access class attribute using instance