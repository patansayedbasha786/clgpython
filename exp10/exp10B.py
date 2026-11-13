queue = []
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = input("Enter element: ")
        queue.append(x)
        print("Element inserted")
    elif ch == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted element:", queue.pop(0))
    elif ch == 3:
        print("Queue:", queue)
    elif ch == 4:
        break
    else:
        print("Invalid choice")
