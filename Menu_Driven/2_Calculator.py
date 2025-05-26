# Menu driven program for calculator where we add, divide, multiply and substract

def c_add(a,b):
    k=a+b
    print("Addition of A and B:", k)

def c_substract(a, b):
    k=a-b
    print("Substraction of A and B:", k)

def c_multiplication(a, b):
    k=a*b
    print("Multiplication of A and B:", k)

def c_division(a, b):
    k=a/b
    print("Divison of A and B:", k)

def c_modulo(a, b):
    k=a//b
    print("Modulus of A and B:", k)

print("Calculator for Addition, Substraction, Multiplication, Division and Modulus")


while True:
    print('1. Addition.')
    print('2. Substraction.')
    print('3. Multiplication.')
    print('4. Division.')
    print('5. Modulus.')
    
    choice=int(input("\nEnter the option :"))
    if choice==1:
        a=int(input("\nEnter the value of a:"))
        b=int(input("\nEnter the value of b:"))
        c_add(a, b)
    
    elif choice==2:
        a=int(input("\nEnter the value of a:"))
        b=int(input("\nEnter the value of b:"))
        c_substract(a, b)
    
    elif choice==3:
        a=int(input("\nEnter the value of a:"))
        b=int(input("\nEnter the value of b:"))
        c_multiplication(a, b)
    elif choice==4:
        a=int(input("\nEnter the value of a:"))
        b=int(input("\nEnter the value of b:"))
        c_division(a, b)

    elif choice==5:
        a=int(input("\nEnter the value of a:"))
        b=int(input("\nEnter the value of b:"))
        c_modulo(a, b)
    
    elif choice==6:
        print("Thank you! please come again.")
        break
    else:
        print('Incorrect Choice.')