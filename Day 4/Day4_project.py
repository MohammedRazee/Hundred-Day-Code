import random

rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
      '''

paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)

'''

scissors = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)

'''

game = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(f"{game[user]}\n")

system = random.randint(0, 2)
print(f"Computer chose:\n {game[system]}")


if ( user == system ):
    print("Draw")

elif user == 0:
    if system == 1:
        print("You lose")
    else:
        print("You win!")

elif user == 1:
    if system == 2:
        print("You lose")
    else:
        print("You win!")

elif user == 2:
    if system == 0:
        print("You lose")
    else:
        print("You win!")

else:
    print("Invalid input")
