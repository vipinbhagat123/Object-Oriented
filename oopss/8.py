#You can modify properties on objects like this:

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1=person('vipin', '21')
p1.age=22                   # You can modify properties on objects like this:            
print(p1.name)
print(p1.age)