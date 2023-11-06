alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "z",
]


def hash(hash_text, shift_amount, direction):
    hash_product = ""
    if direction == "decode":
        shift_amount *= -1

    for letter in hash_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            hash_product += alphabet[new_position]

        else:
            hash_product += letter

    print(f"The {direction}d text is {hash_product}")


while not False:
    hash_direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    shift_number = shift % 26

    hash(hash_text=text, shift_amount=shift_number, direction=hash_direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        print("Goodbye")
        break
