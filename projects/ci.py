# Compound interest

years = int(input("Enter the number of years: "))
principal = int(input("Enter the principal: "))
rate = int(input("Enter the rate: "))
print("1. Half yearly")
print("2. Quarterly")
print("3. Yearly")
compounded = int(input("Enter the number of times compounded (half yearly, quarterly or yearly): "))
amount = 0
if compounded == 1:
    amount = principal * (1 + rate/2/100)**(2*years)
elif compounded == 2:
    amount = principal * (1 + rate/4/100)**(4*years)
elif compounded == 3:
    amount = principal * (1 + rate/100)**years

print("Amount: ", amount)

ci = amount - principal
print("Compound interest: ", ci)