def get_user_input():
    while True:
        try:
            user_input = input("Enter 'a' or 'b': ").lower()
            if user_input not in ['a', 'b']:
                raise ValueError("Invalid input. Please enter 'a' or 'b'.")
            return user_input
        except ValueError as e:
            print(e)

# Keep asking until valid input is received
choice = get_user_input()
print(f"You entered: {choice}")
