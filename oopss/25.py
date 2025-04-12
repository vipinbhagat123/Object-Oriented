# Function inside a function

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    print(myinnerfunc())
print(myfunc())