# python Inheritance

# Inheritance allows us to define a class that inherits all the methodsand properties from another classs. 
# Parent class is the class being inherited from,also called base class.
# # Child class is the class that inherits from another class, also called derived class. 


class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x=person('john', 'Doe')
print(x.printname())