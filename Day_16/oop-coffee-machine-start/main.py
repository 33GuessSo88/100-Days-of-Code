from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    customer_order = input(f"What is your order? {menu.get_items()}")
    if customer_order == "off":
        is_on = False
    elif customer_order == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(customer_order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                #coffee_maker.report()

#Fuck me, that was hard. OOP.
#I got close to solving it, didn't realize make payment method took money.
