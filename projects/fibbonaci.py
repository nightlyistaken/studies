# Fibbonaci sequence 
number = int(input("Enter a number: "))
a = 0
b = 1
for i in range(number):
    print(a)
    c = a + b
    a = b
    b = c