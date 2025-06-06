# Menu driven program to calculate perimeter and area of different shapes

# Declaring all the required functions with the calculations of perimeter of different shapes

def per_circle(radius):
    perimeter = 2 * 3.14 * radius
    print("Perimeter of circle :", perimeter)

def per_triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    print("Perimeter of Triangle: ", perimeter)

def per_rectangle(height, width):
    perimeter = 2 * (height + width)
    print("perimeter of Rectangle:", perimeter)

def per_square(side):   
    perimeter = 4*side
    print("perimeter of a square:", perimeter)

#Declaring all the required functions with the calculations of area of different shapes

def a_circle(radius):
    area = 3.14 * radius * radius
    print("Area of circle :", area)

def a_triangle(base, height):
    area = base * height/2
    print("Area of a Triangle:", area)

def a_rectangle(height, width):
    area = height * width
    print("Area of Rectangle:", area)

def a_square(side):
    area = side * side
    print("Area of square:", area)

# Heading of menu-driven approach

print("\nWELCOME TO MENSURATION PROGRAM! TRY CALCULATING PERIMETER AND AREA OF DIFFERENT GEOMETRIC SHAPES.")

# Using the while loop to print menu list

while True:
    print('\nMenu')
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Square")
    print("5. Exit")
    shape_choice=int(input("\nEnter your choice of shape for calculation:"))


    if shape_choice == 1:
        while True:
            print("\n1. Calculate Perimeter of circle")
            print("2. Calculate area of circle")
            print("3. Exit")
            choice1 = int(input("\nEnter choice for calculation : "))
            # calling the relevant method based on users choice using if-else loop

            if choice1==1:
                radius = int(input("\Enter Radius of Circle:"))
                per_circle(radius)
            elif choice1==2:
                radius = int(input("Enter Radius of circle:"))
                a_circle(radius)
            elif choice1==3:
                break
            else:
                print("Incorrect Choice!")

    elif shape_choice == 2:
        while True:
            print("\n1. Calculate perimeter of Triangle")
            print("2. Calculate area of Triangle")
            print("3. Exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                side1 = int(input("Enter length of side1: "))
                side2 = int(input("Enter length of side2: "))
                side3 = int(input("Enter length of side3: "))
                per_triangle(side1,side2,side3)
            elif choice1 == 2:
                base = int(input("Enter base of traingle: "))
                height = int(input("Enter height of traingle: "))
                a_triangle(base, height)
            elif choice1 == 3:
                break
            else:
                print("Incorrect Choice!")
        
    elif shape_choice == 3:
        while True:    
            print("\n1. Calculate perimeter of Rectangle")
            print("2. Calculate area of Rectangle")
            print("3. Exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                height = int(input("Enter height of rectangle: "))
                width = int(input("Enter width of rectangle: "))
                per_rectangle(height,width)
            elif choice1 == 2:
                height = int(input("Enter height of rectangle: "))
                width = int(input("Enter width of rectangle: "))
                a_rectangle(height,width)
            elif choice1 == 3:
                break
            else:
                print("Incorrect Choice!")
    
    elif shape_choice == 4:
        while True:
            print("\n1. Calculate perimeter of Square")
            print("2. Calculate area of Square")
            print("3. Exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                side = int(input("Enter side of square: "))
                per_square(side)
            elif choice1 == 2:
                side = int(input("Enter side of square: "))
                a_square(side)
            elif choice1 == 3:
                break
            else:
                print("Incorrect Choice!")
                
    #exit condition to get out of the while loop
    elif shape_choice == 5:
        print("Thank You! See you again.")
        break
    
    else:
        print("Incorrect Choice. Please, try again.")
