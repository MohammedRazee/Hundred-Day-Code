import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your passwork?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

for let in range(0, nr_letters):
    password.append(random.choice(letters))

for let in range(0, nr_symbols):
    password.append(random.choice(symbols))

for let in range(0, nr_numbers):
    password.append(random.choice(numbers))


# Atleast I know I can use my brain... That's news

# temp = password.copy()

# print("Here is your password:", end=' ')
# for n in password:
#     printer = random.choice(temp)
#     print(printer, end='')
#     temp.remove(printer)



random.shuffle(password)

final_pass = ""

for char in password:
    final_pass += char

print(f"Here is your password: {final_pass}")
