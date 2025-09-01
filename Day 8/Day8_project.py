import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(option, original_text, shift_amount):
    output = ""

    if option == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position = shifted_position % len(alphabet)
            output += alphabet[shifted_position]
        else:
            output += letter

    print(f"Here is your {option}d result: {output}")


should_continue = True

while (should_continue):
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(direction, text, shift)
    else:
        print("Invalid Input!")

    choice = input("\nType 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if choice == "no":
        should_continue = False
        print("\n\nBye Bye\n")
        print(art.byebye)
        
