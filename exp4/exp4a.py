ID=[10,20,30,40,50]
print(ID)
while True:
    print("Operation on a list")
    print("1.addition")
    print("2.Insertion")
    print("3.Slicing")
    print("4.Deletion")
    ch=input("Enter your Choice:")
    if ch == "1":
        n=int(input("Number of elements to add"))
        for i in range(0,n):
            data=int(input("Enter data:"))
            ID.append(data)
        print(ID)
    elif ch == "2":
        print("Insert element in list")
        pos=int(input("Enter position:"))
        data=int(input("Enter data:"))
        ID.insert(pos,data)
        print(ID)
    elif ch == "3":
        print("Slicing operation")
        start=int(input("Enter start position:"))
        endp=int(input("Enter end position:"))
        print(ID[start:endp])
    elif ch == "4":
        print("Deletion operation")
        pos=int(input("Enter index position of item to delete:"))
        del ID[pos]
        print("List after deletion:")
        print(ID)
    else:
        print("Invalid option")
        break
