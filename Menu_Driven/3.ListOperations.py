mylist=[22,4,16,38,13]
choice=0
while True:
    print("The list 'mylist' has the following elements", mylist)
    print('\nL I S T O P E R A T I O N S')
    print("1. Append an element.")
    print("2. Insert an element at the desired position.")
    print('3. Append a list to the given list.')
    print('4. Modify an existing element.')
    print('5. Delete an existing element by its position.')
    print('6. Delete an existing element by its value.')
    print('7. Sort the list in asscending order.')
    print('8. Sort the list in descending order.')
    print('9. Display the list.')
    print('10. Exit')

    choice = int(input('Enter you choice (1-10):'))
    # append element
    if choice==1:
        element = int(input("Enter the element to be appended:"))
        mylist.append(element)
        print("The element has been appended\n")

    elif choice==2:
        element = int(input("Enter the element to be inserted: "))
        pos = int(input("Enter the position:"))
        mylist.insert(pos,element)
    