from menu import MENU
from resources import resources


def check_resources(order):
    """returns True if all resources > all menu items, False if not"""
    if resources['water'] <= MENU.get(order).get('ingredients').get('water', 0):
        return False

    if resources['milk'] <= MENU.get(order).get('ingredients').get('milk', 0):
        return False

    if resources['coffee'] <= MENU.get(order).get('ingredients').get('coffee', 0):
        return False
    else:
        return True


def subtract_resources(order):
    """subtracts the order ingredients from the resources and returns it"""
    resources['water'] = resources['water'] - MENU.get(order).get('ingredients').get('water', 0)
    resources['milk'] = resources['milk'] - MENU.get(order).get('ingredients').get('milk', 0)
    resources['coffee'] = resources['coffee'] - MENU.get(order).get('ingredients').get('coffee', 0)
    return resources


def make_change(money_paid, cost):
    """returns calculated change"""
    change = money_paid - cost
    return change


def find_negative_resource(x, y):
    for key, value in x.items():
        if value < 1:
            return key


def print_report():
    for key, value in resources.items():
        if key == 'water' or key == 'milk':
            print(key, ":", " ", value, "ml")
        elif key == 'coffee':
            print(key, ":", " ", value, "g")
        else:
            print(key, ":", " $", value)


another_order = True
sales = 0

while another_order:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print_report()
    elif not check_resources(order):
        if resources['water'] <= MENU.get(order).get('ingredients').get('water', 0):
            print("There isn't enough water.")
        elif resources['coffee'] <= MENU.get(order).get('ingredients').get('coffee', 0):
            print("There isn't enough coffee.")
        else:
            print("There isn't enough milk.")
    else:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        money_paid = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        drink_cost = MENU[order]['cost']
        if money_paid >= drink_cost and check_resources(order):
            print(f"Here is ${round(make_change(money_paid, drink_cost), 2)} in change.")
            print(f"Here is your {order}. Enjoy!")
            subtract_resources(order)
            sales += money_paid
            resources["sales"] = sales

        else:
            print("Sorry, that's not enough money. Money refunded.")
