import math

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def OptimizedInput():
    while True:
        try:
            das_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if (das_input not in MENU) and (das_input not in ["off", "report"]):
                raise ValueError ("""Enter a valid option please: 
                1. Espresso
                2. Cappuccino
                3. Latte
                4. Report (To check available resources in the machine)
                5. Off (To turn off the machine)""")
            return das_input
        except ValueError as e:
            print(e)

def DisplayReport(total_money):
    print(f"""
Water: {resources["water"]}
Milk: {resources["milk"]}
Coffee: {resources["coffee"]}
Money: ${total_money}""")
    

def CheckResource(request):
    req_water = MENU[request]["ingredients"]["water"]
    req_coffee = MENU[request]["ingredients"]["coffee"]
    if request != "espresso":
        req_milk = MENU[request]["ingredients"]["milk"]
        if req_milk > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False

    if req_water > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif req_coffee > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    
    return True

def GetMoney(request, current_amount):
    print("Please insert coins\n")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))

    paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    coffee_cost = MENU[request]["cost"]

    if paid < coffee_cost:
        print("Insufficient funds!")
        return current_amount
    else:
        change = paid - coffee_cost
        change = round(change, 2)
        print(f"Here is ${change} in change")
        x = current_amount + coffee_cost
        return x
    

def MakeCoffee(request):
    source = MENU[request]["ingredients"]
    used_water = source["water"]
    used_coffee = source["coffee"]

    if request != "espresso":
        used_milk = source["milk"]
        resources["milk"] -= used_milk
    
    resources["coffee"] -= used_coffee
    resources["water"] -= used_water




def CoffeeMachine():
    money = 0

    while True:
        user_input = OptimizedInput()
        if user_input == "report":
            DisplayReport(money)
        elif user_input == "off":
            return
        elif user_input in MENU:
            if CheckResource(user_input):
                temp = money
                money = GetMoney(user_input, money)
                if money != temp:
                    MakeCoffee(user_input)
                    print(f"Here is your {user_input}. Enjoy!")

CoffeeMachine()
