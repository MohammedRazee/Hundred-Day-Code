import art
import os
from random import choice
from game_data import data

def optimize_input():
    '''Forces the user to choose between the correct options'''
    while True:
        try:
            user_input = input("Who has more followers? Type 'A' or 'B' ").lower()
            if user_input not in ['a', 'b']:
                raise ValueError("Choice is pretty simple and there is only two.")
            return user_input
        except ValueError as e:
            print(e)


def play_game(replay):
    '''The gameplay'''

    score = 0
    player_a = choice(data)

    while(True):
        os.system('cls')
        print(art.logo)
        player_b = choice(data)

        if replay != -1:
            print(f"High Score: {replay}")

        followers = {
            'a': player_a['follower_count'],
            'b': player_b['follower_count'],
        }

        print(f"Compare A: {player_a["name"]}, {player_a["description"]}, from {player_a["country"]}")
        print(f"\n {art.vs}")
        print(f"Compare B: {player_b["name"]}, {player_b["description"]}, from {player_b["country"]}")

        
        user_choice = optimize_input()


        target = max(followers.values())
        print(target)
        if followers[user_choice] == target:
            score += 1
            print(f"You're right! Current score: {score}")
            player_a = player_b
        else:
            return score

    

def main_game():
    '''Main function where the game is played'''

    high_score = -1

    running = True
    while(running):

        player_score = play_game(high_score)
        high_score = player_score

        os.system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {player_score}")
        repeat = input("\nDo you want to keep playing? Type 'y' or 'n'").lower()

        if repeat == 'n':
            running = False


main_game()
