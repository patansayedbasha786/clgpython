def display_numbers():
    for i in range(1000, 2001):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=" ")
display_numbers()
