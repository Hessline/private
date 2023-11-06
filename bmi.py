#BMI program

#get weight from user (kilos)
weight = float(input("Enter your weight: "))

#get height from user (height as m)
height = float(input("Enter your height: "))

#calculate BMI
BMI = weight / (height ** 2)

#display a message indicating whether the person is underweight, healthy weight, overweight, or obese
if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are healthy weight")
elif BMI < 30:
    print("You are overweight")
