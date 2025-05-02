# Class Variables

# These are the variables that are shared across all instance of a class. 

# Instance variables

# Variables that are unique to each instance(object) of a class.

class Dog:
    # class Variable

    species = 'Canine'  # class attribute

    def __init__(self, name, age):
        # Instance Variable
        self.name = name # Instance Attributes
        self.age = age   # Instance Attributes

# Create objects

dog1 = Dog('Buddy', 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables

print(dog1.species) # (class Variable)
print(dog1.name)    # (Instance Variable)
print(dog2.name)    # (Instance Variable)

# Modify instance variables

dog1.name = 'Max'
print(dog1.name)    # (updated instance variable)

# Modify class Variables
Dog.species = 'Feline'
print(dog1.species) # (updated class variable)
print(dog2.species)


Explanation:

#  Class Variable (species): Shared by all instances of the class. Changing Dog.species affects all objects, as it’s a property of the class itself.
#  Instance Variables (name, age): Defined in the __init__ method. Unique to each instance (e.g., dog1.name and dog2.name are different).
#  Accessing Variables: Class variables can be accessed via the class name (Dog.species) or an object (dog1.species). Instance variables are accessed via the object (dog1.name).
#  Updating Variables: Changing Dog.species affects all instances. Changing dog1.name only affects dog1 and does not impact dog2.