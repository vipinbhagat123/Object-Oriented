# Delete Object Properties

# you can delete properties on objects by using the del keyword:

class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1=person('Vipin', 22)
del p1.age
print(p1.age)