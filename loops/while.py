"""
While loop syntax
initialisation
while <condition>:
    loop body
    operation
"""
# Print first 10 natural numbers
print("First 10 natural numbers:")
i = 0
while i < 10:
    print(i)
    i += 1


# Print squares of first 10 natural numbers
print("Squares of first 10 natural numbers:")
i = 0
while i < 10:
    print(i*i)
    i += 1

# Print table of a number
print("Table of a number:")
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number, " x ", i, " = ", number * i)
    i += 1


# Loop with else
print("Loop with else:")
num1 = int(input("Enter the lower limit: "))
num2 = int(input("Enter the upper limit: "))
even = 0
odd = 0

for i in range(num1,num2+1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
else:
    print("Loop is terminated successfully")

print("The sum of all the even numbers in the given series is: ", even)
print("The sum of all the odd numbers in the given series is: ", odd)