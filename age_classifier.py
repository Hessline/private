#asks the user to enter a person’s age
Age = int(input("Enter your age: "))

#display a message indicating whether the person is an infant, a child, a teenager, or an adult
if Age < 1:
    print("You are an infant")
elif Age < 13:
    print("You are a child")
elif Age < 20:
    print("You are a teenager")
elif Age > 20:
    print("You are an adult")

