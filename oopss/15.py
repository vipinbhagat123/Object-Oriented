# Python also has a super() function that will make the child class inherit all the methods and properties from its parent

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = student('Mike', 'olsen')
print(x.printname())