
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("What is your first number? "))
for key in operations:
    print(key)

should_continue = True
while should_continue:
    operator = input("What operator would you like from the list above? ")
    num2 = float(input("What is your next number? "))

    answer = operations.get(operator)(num1, num2)
    print(f"{num1} {operator} {num2} is {answer}")
    y_or_n = input("Would you like to continue? y or n ")
    if y_or_n == "n":
        should_continue = False
        print("Thank you for using the calculator.")
    num1 = answer
