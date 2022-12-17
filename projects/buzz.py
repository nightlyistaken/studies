# Buzz number is a number that is divisible by 7 or ends with 7

number = int(input("Enter a number: "))
if number % 7 == 0 or number % 10 == 7:
    print("Buzz 🐝")
else:
    print("Not buzz")