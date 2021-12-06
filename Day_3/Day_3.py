height = float(input("what is your height in m? "))
weight = float(input("what is your weight? "))

bmi = round(weight / height ** 2, 1)

print(f"youre bmi is {bmi}")

if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are normal weight")
elif bmi < 30:
    print("you are overweight")
elif bmi < 35:
    print("you are a big diesel")
else:
    print("you are about to die")
