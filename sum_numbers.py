#Entering data and making additions
number = 1.0
total = 0.0

while number > 0:
    number = float(input("Enter a number: "))
    if number > 0:
        total += number
    else:
        pass

print(f"The total is {total:.2f}")