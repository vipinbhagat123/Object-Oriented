class Person:           # creating a class
    def __init__(self, name, age):      # constructor method
        self.name = name                # instance variable
        self.age = age                  # instance variable 
p1 = Person("John", 36)                 # creating an object of the class
print(p1.name)              # accessing the instance variable   
print(p1.age)                   # accessing the instance variable

