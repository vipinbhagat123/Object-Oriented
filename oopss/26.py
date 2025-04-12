# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.

x = 300
def myfunc():
    print(x)
print(myfunc())
print(x)