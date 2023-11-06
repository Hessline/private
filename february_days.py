#asks the user to enter a year
year = int(input("Enter a year: "))

#display the number of days in February that year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(29)
        else:
            print(28)
    else:
        print(29)

