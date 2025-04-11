class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)
x=student('mike', 'olsen')
print(x.printname())