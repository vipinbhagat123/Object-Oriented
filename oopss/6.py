# object methods
# Objects can also contain methods. 
# Methods in objects are functions that belong to the object.

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = person("John", 36)
p1.myfunc()
