import sympy

# Entering number to ckeck
number = int(input("Please enter a integer to ckeck: "))

if sympy.isprime(number):
    print(number, "is prime")
else:
    print(number, "is not prime")