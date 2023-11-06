#ask the user to enter the charge for the food
Charge = float(input("Enter the charge for the food: "))

#calculate the amounts of a 18 percent tip and 7 percent sales tax
Tip = Charge * 18 / 100
Tax = Charge * 7 / 100

#Display each of these amounts and the total
print("The total charge is", Charge)
print("The total tip is", Tip)
print("The total tax is", Tax)
print("The total is", Charge + Tip + Tax)

print("The total is", Charge + Tip + Tax)


