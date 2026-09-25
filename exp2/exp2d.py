num = int(input("Enter a number: "))

reverse = 0
sum_digits = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    sum_digits = sum_digits + digit
    num = num // 10

print("Reverse =", reverse)
print("Sum of digits =", sum_digits)
