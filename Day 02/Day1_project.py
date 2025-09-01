print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $")) #Type conversion during accepting the values is sugested

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

no_of_people = int(input("How many people to split the bill? "))

indi_bill = tip / 100 * total_bill + total_bill

indi_bill /= no_of_people

print(f"Each person should pay: ${round(indi_bill, 2)}")