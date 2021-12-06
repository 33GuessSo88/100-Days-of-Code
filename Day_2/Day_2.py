print("Welcome to the tip calculator. ")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip woudl you like to give? "))
no_of_people = int(input("How many people to split the bill? "))
per_person_cost = total_bill * (1 + (tip_percentage/100) ) / no_of_people
per_person_cost = round(per_person_cost, 2)
per_person_cost = "{:.2f}".format(per_person_cost) #rounding when result is a whole number
print(f"Each person should pay ${per_person_cost}")