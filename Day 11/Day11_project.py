from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def ace_check(card_list):
    """Checks if there is an Ace in the card drawn."""
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)


def blackjack():
    """Plays a game of blackjack"""
    user_card = []
    house_card = []

    for _ in range(2):
        user_card.append(random.choice(cards))
        house_card.append(random.choice(cards))

    user_score = sum(user_card)
    house_score = sum(house_card)

    ace_check(user_card)


    round = True

    while round:
        user_score = sum(user_card)
        print(f"  Your cards: {user_card}, current score: {user_score}")
        print(f"  Computer's first card: {house_card[0]}")

        if user_score < 21:
            hit_pass = input("\nType 'y' to get another card. Type 'n' to pass: ").lower()

        if user_score >= 21 or hit_pass != "y":
            round = False

            while house_score < 16:
                house_card.append(random.choice(cards))
                ace_check(house_card)
                house_score = sum(house_card)

            print(f"  Your final hand: {user_card}, final score: {user_score}")
            print(f"  Computer's final hand: {house_card}, final score: {house_score}")

            if user_score > 21:
                return "You went over. You Lose. 😭"
            
            elif user_score == 21:
                return "Blackjack! You Win! 😎"

            elif house_score == 21:
                return "Lose, opponent has Blackjack 😱"

            elif house_score > 21:
                return "Opponent went over. You Win! 😁"
            
            elif user_score > house_score:
                return "You Win! 😃"
            
            elif user_score == house_score:
                return "Draw 🙃"
            
            else:
                return "You Lose 😤"
            
        elif hit_pass == "y":
            user_card.append(random.choice(cards))
            ace_check(user_card)
            



game = True
continue_game = "y"

while game:
    continue_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if continue_game == "n":
        game = False
    
    else:
        os.system('cls')
        print(f"{logo}\n")
        print("\n" + blackjack())

