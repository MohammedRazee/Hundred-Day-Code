import art
import os

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

def calc(f_num):
    for key in operations:
        print(f"{key}")

    operator = input("Pick an operation: ")

    num2 = float(input("What's the next number?: "))

    return operations[operator](f_num, num2)



calculations = True
repeater = "n"
stored_number = 0

while calculations:
    if repeater == "y":
        stored_number = calc(stored_number)
        print(stored_number)
    else:
        os.system("cls")
        print(art.logo)
        num1 = float(input("What's the first number?: "))
        stored_number = calc(num1)
        print(stored_number)

    repeater = input(f"Type 'y' to continue with {stored_number}, or type 'n' to start a new calculation. Type 'exit' to leave the calculator: ").lower()
    
    if repeater == "exit":
        calculations = False


