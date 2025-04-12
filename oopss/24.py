# Local Scope

# A variable created inside a function belongs to the local scope of that function. and can only be used inside that function.


def myfunc():
    x=300
    print(x)
print(myfunc())