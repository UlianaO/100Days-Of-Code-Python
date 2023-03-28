# This is a simple coffee machine to put a few of OOP principles into practice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
turned_on = True

while turned_on:
    options = menu.get_items()
    print()
    choice = input(f"What would you like to drink? ({options}). Type 'report' or 'off' to turn off the machine: ")
    if choice == "report":
        # Print reports
        money_machine.report()
        coffee_maker.report()
    elif choice == "off":
        turned_on = False
    else:
    # Check if ingredients are enough to make coffee
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)