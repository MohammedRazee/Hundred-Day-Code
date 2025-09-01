import random


stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""

for n in chosen_word:
    placeholder += "_"

print(placeholder)

lives = 6
corrected_letters = []
result = "" 

while result != chosen_word and lives > 0:
    result = ""
    guess = input("\nGuess a letter: ").lower()
    for letter in chosen_word:
        if guess == letter:
            result += guess
            if letter not in corrected_letters:
                corrected_letters.append(guess)
        elif letter in corrected_letters:
            result += letter
        else:
            result += "_"
    if guess not in chosen_word:
        print("\nWrong guess")
        lives -= 1
    print(stages[6 - lives])
    print(result)

if lives != 0:
    print("\n\nYou win!")
else:
    print("\n\nNo more guesses you lose")
