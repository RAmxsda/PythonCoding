# to generate random password
import random
import string


def generate_password(length):
    # define the length of the password
    length = int(input("Enter the length of the password: "))
    # define the characters to use in the password

    characters = string.ascii_letters + string.digits + string.punctuation

    # generate the password

    password = "".join(random.choice(characters) for i in range(length))

    # print the password

    print(password)


generate_password(length=8)
