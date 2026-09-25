n=int(input("Enter n:"))
if n ==1:
    print(n,"not a prime number")
elif n == 2:
    print(n,"is a prime number")
elif n == 3:
    print("prime numbers are:")
    for i in range(2,n+1):
        print(i,end=" ")
else:
    print("prime numbers are:")
    for i in range(1,n+1):
        c=0
        for j in range(1,i+1):
            if i%j == 0:
                c=c+1
        if c==2:
            print(i,end=" ")
