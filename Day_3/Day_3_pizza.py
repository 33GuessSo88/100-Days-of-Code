print("welcome to pit viper pizza!")
bill = 0
size = input("would you like S, M, or L pizza? ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

pepperoni = input("would you like pepperoni? Y or N ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

cheese = input("would you like extra cheese? Y or N ")
if cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")