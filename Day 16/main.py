from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

def Run_Machine():
    order = input(f"What would you like? {menu.get_items()}: ").lower()
    if order == "off":
        return False
    elif order == "report":
         maker.report()
         money.report()
    else:
        ordered_drink = menu.find_drink(order)
        if ordered_drink is not None:
            if maker.is_resource_sufficient(ordered_drink):
                    if money.make_payment(ordered_drink.cost):
                        maker.make_coffee(ordered_drink)
    return True

running = True
while(running):
    running = Run_Machine()
    