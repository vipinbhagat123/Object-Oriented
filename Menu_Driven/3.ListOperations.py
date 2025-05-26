myList = [22, 4, 16, 38, 13]

choice = 0
while True:
    print("\nThe list 'myList' has the following elements:", myList)
    print("\nL I S T  O P E R A T I O N S")
    print(" 1. Append an element")
    print(" 2. Insert an element at the desired position")
    print(" 3. Append a list to the given list")
    print(" 4. Modify an existing element")
    print(" 5. Delete an existing element by its position")
    print(" 6. Delete an existing element by its value")
    print(" 7. Sort the list in ascending order")
    print(" 8. Sort the list in descending order")
    print(" 9. Display the list")
    print("10. Exit")
    
    choice_input = input("ENTER YOUR CHOICE (1-10): ")
    if not choice_input.isdigit():
        print("Invalid input! Please enter a number between 1 and 10.")
        continue
    choice = int(choice_input)

    if choice == 1:
        element = input("Enter the element to be appended: ")
        if element.isdigit():
            myList.append(int(element))
            print("The element has been appended\n")
        else:
            print("Please enter a valid integer.\n")

    elif choice == 2:
        element = input("Enter the element to be inserted: ")
        pos = input("Enter the position: ")
        if element.isdigit() and pos.isdigit():
            pos = int(pos)
            if 0 <= pos <= len(myList):
                myList.insert(pos, int(element))
                print("The element has been inserted\n")
            else:
                print("Invalid position!\n")
        else:
            print("Invalid input. Please enter integers only.\n")

    elif choice == 3:
        user_input = input("Enter elements separated by commas (e.g., 1,2,3): ")
        parts = user_input.split(',')
        all_ints = True
        for x in parts:
            if not x.strip().isdigit():
                all_ints = False
                break
        if all_ints:
            newList = [int(x.strip()) for x in parts]
            myList.extend(newList)
            print("The list has been appended\n")
        else:
            print("Invalid input. All elements must be integers.\n")

    elif choice == 4:
        i = input("Enter the position of the element to be modified: ")
        if i.isdigit():
            i = int(i)
            if 0 <= i < len(myList):
                newElement = input("Enter the new element: ")
                if newElement.isdigit():
                    oldElement = myList[i]
                    myList[i] = int(newElement)
                    print(f"The element {oldElement} has been modified to {newElement}\n")
                else:
                    print("Invalid input. Please enter an integer.\n")
            else:
                print("Invalid position!\n")
        else:
            print("Invalid input. Please enter a valid number.\n")

    elif choice == 5:
        i = input("Enter the position of the element to be deleted: ")
        if i.isdigit():
            i = int(i)
            if 0 <= i < len(myList):
                element = myList.pop(i)
                print(f"The element {element} has been deleted\n")
            else:
                print("Invalid position!\n")
        else:
            print("Invalid input. Please enter a number.\n")

    elif choice == 6:
        element = input("Enter the element to be deleted: ")
        if element.isdigit():
            element = int(element)
            if element in myList:
                myList.remove(element)
                print(f"The element {element} has been deleted\n")
            else:
                print(f"Element {element} is not present in the list\n")
        else:
            print("Invalid input. Please enter an integer.\n")

    elif choice == 7:
        myList.sort()
        print("The list has been sorted in ascending order\n")

    elif choice == 8:
        myList.sort(reverse=True)
        print("The list has been sorted in descending order\n")

    elif choice == 9:
        print("The list is:", myList)

    elif choice == 10:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 10.")

    input("Press Enter to continue...")

