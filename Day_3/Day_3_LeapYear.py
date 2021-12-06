year = int(input("type in a year "))

if year % 4 != 0:
    print("this is not a leap year 4")
elif year % 100 == 0:
    if year % 400 == 0:
        print("this is a leap year 400")
    else:
        print("this is not a leap year 400")
else:
    print("this is a leap year end")

