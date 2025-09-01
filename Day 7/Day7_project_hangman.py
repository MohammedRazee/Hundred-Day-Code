import random
import hangman_art
import hangman_words

print(hangman_art.logo)

# Initialization

art = hangman_art.stages

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
size = len(chosen_word)

output = []
lives = 6
game_over = False
output_str = ""

# Getting the output ready 
for n in chosen_word:
    output.append("_")

# Executing game code

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    guess = input("\nGuess a letter:  ")
    if guess in output:
        print(f"\nYou have already guessed {guess}")

    elif guess not in chosen_word:
        print(f"\nYou guessed {guess}, that is not in the word. You lose a life")
        lives -= 1

    else:
        for index in range(size):
            if chosen_word[index] == guess:
                output[index] = guess
        
    output_str = "".join(output)
    print(f"\nWord to guess:  {output_str}\n")

    if lives == 0:
        print("****************************YOU LOSE****************************")
        game_over = True
    elif output_str == chosen_word:
        print("****************************YOU WIN****************************")
        game_over = True

    print(hangman_art.stages[lives])
    