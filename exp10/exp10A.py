stack = []
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = input("Enter element: ")
        stack.append(x)
        print("Element inserted")
    elif ch == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Deleted element:", stack.pop())
    elif ch == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])
    elif ch == 4:
        print("Stack:", stack)
    elif ch == 5:
        break
    else:
        print("Invalid choice")
