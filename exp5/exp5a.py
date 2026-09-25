telephone_directory = {}
employee_list = []
while True:
    print("\n========== TELEPHONE DIRECTORY ==========")
    print("1. Add Entry")
    print("2. Search Entry")
    print("3. Delete Entry")
    print("4. Update Entry")
    print("5. View Entries")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
 
    if choice == 1:
        name = input("Enter employee name: ")
        phone = input("Enter contact number: ")
        if name in telephone_directory:
            print("Employee already exists.")
        else:
            telephone_directory[name] = phone
            employee_list.append(name)
            print("Entry added successfully.")

    elif choice == 2:
        name = input("Enter employee name to search: ")

        if name in telephone_directory:
            print("Employee Name :", name)
            print("Contact Number:", telephone_directory[name])
        else:
            print("Employee not found.")
    elif choice == 3:
        name = input("Enter employee name to delete: ")
        if name in telephone_directory:
            del telephone_directory[name]
            employee_list.remove(name)
            print("Entry deleted successfully.")
        else:
            print("Employee not found.")
    
    elif choice == 4:
        name = input("Enter employee name to update: ")
        if name in telephone_directory:
            new_phone = input("Enter new contact number: ")
            telephone_directory[name] = new_phone
            print("Contact number updated successfully.")
        else:
            print("Employee not found.")
    
    elif choice == 5:
        if len(telephone_directory) == 0:
            print("Telephone directory is empty.")
        else:
            print("\n------ Employee Contact List ------")
            for name in employee_list:
                print("Name :", name)
                print("Phone:", telephone_directory[name])
                print("--------------------------------")
    
    elif choice == 6:
        print("Exiting Telephone Directory...")
        break
    else:
        print("Invalid choice. Please enter 1 to 6.")
