# Factorial of a number
# example: 5! = 5 * 4 * 3 * 2 * 1

number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)
