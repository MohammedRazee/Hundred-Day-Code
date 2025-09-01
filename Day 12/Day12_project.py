# Number Guessing Game

from art import logo
from random import randint
import os

def create_number():
    '''Generates a random number'''
    return randint(1, 100)

def game(level):
    '''Plays the Game'''
    target = create_number()
    attempts = 10
    if level == "hard":
        attempts = 5

    while True:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess == target:
            return f"You got it! The number is {target}"
        
        if attempts == 1:
            return "You've run out of guesses. You Lose!"

        if guess > target:
            print("Too High. \nGuess Again.")

        elif guess < target:
            print("Too Low. \nGuess Again.")

        
        attempts -= 1


# Main code running here           

choice = "y"
run_game = True

while run_game:
    choice = input("Do you want to play the Number Guessing Game. Type 'y' or 'n': ").lower()
    if choice == "n":
        run_game = False

    else:
        os.system('cls')
        print(logo)
        print("\n")
        print("I'm thinking of a number between 1 and 100")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        print(game(difficulty))
