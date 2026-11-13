import os
print("1. List Directory")
print("2. Create Directory")
print("3. Rename Directory or File")
print("4. Remove Directory or File")
ch = int(input("Enter your choice: "))
if ch == 1:
    print(os.listdir())
elif ch == 2:
    name = input("Enter directory name: ")
    os.mkdir(name)
    print("Directory created successfully")
elif ch == 3:
    old = input("Enter old name: ")
    new = input("Enter new name: ")
    os.rename(old, new)
    print("Renamed successfully")
elif ch == 4:
    name = input("Enter name to remove: ")
    if os.path.isfile(name):
        os.remove(name)
    else:
        os.rmdir(name)
    print("Removed successfully")
else:
    print("Invalid choice")
