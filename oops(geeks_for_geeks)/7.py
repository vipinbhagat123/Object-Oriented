# Python Polymorphism

# Polymorphism allows methods to have the same name but behave differently based on the object context.

# Types of Polymorphism

# Compile-Time Polymorphism: This type of polymorphism is determined during the compilation of the program. It allows methods or operators with the same name to behave differently based on their input parameters or usage. It is commonly referred to as method or operator overloading.

# Run-Time Polymorphism: This type of polymorphism is determined during the execution of the program. It occurs when a subclass provides a specific implementation for a method already defined in its parent class, commonly known as method overriding.

class Dog:
    def sound(self):
        print("Dog Sound")  # Default implementation

# Run-Time Polymorphism : Method Overriding
class Labrador(Dog):
    def sound(self):
        print("Labrador Barks")  # Overridden parent method

class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")  # Overridden parent method

# Compile-Time polymorphism : Method Overloading Mimic

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c      # Support multiple ways to call add()

# Run-Time Poymorphism

dogs=[Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound() # Calls the appropriate sound method based on the object type

# Compile-Time polymorphism (mimicked using default arguments)

calc = Calculator()
print(calc.add(5, 10))  # Two arguments
print(calc.add(5, 10, 15))  # Three arguments