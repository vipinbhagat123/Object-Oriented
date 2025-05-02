# An Object is an instance of a class. It represents a specific implementation of the class and holds its own data.

#  An object consists of:

#  State: It is represented by the attributes and reflects the properties of an object.
#  Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
#  Identity: It gives a unique name to an object and enables one object to interact with other objects.

class Dog:
    species = 'Canine'  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
dog1 = Dog("Buddy", 3)
print(dog1.name)
print(dog1.age)