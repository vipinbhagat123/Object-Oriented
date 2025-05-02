# __init__ method is the constructor in python, automaticall called when a new object is created.
# It is used to initialize the attributes of the object.


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = Dog("Buddy", 3)
print(dog1.name)  # Output: Buddy