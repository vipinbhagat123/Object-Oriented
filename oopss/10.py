# Delete Objects
# You can delete objects by using the del keyword:

class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def myfunc():
        print("Hello World")
p1=person('vipin', 22)
del p1
print(p1.age)