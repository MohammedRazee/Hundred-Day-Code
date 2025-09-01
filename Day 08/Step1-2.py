alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


def ceaser(choice, original_text, shift_amount):
    if choice == "encode":
        cipher_text =""

        for letter in original_text:
            index = alphabet.index(letter)
            index += shift_amount

            # My way

            # if index < 26:
            #     cipher_text += alphabet[index]
            # else:
            #     index = index - 26
            #     cipher_text += alphabet[index]

            # Smarter way

            index %= len(alphabet)
            cipher_text += alphabet[index]

        print(f"Here is the encoded result: {cipher_text}")

    # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
    # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
    #  by the shift amount and print the decrypted text.
    # TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
    #  Use the value of the user chosen 'direction' variable to determine which functionality to use.

    if choice == "decode":
        decoded_text = ""
        for letter in original_text:
            index = alphabet.index(letter)
            index -= shift_amount

            decoded_text += alphabet[index]

        print(f"Here is the decoded result: {decoded_text}")


ceaser(direction, text, shift)


