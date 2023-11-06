# Chippers code to encode

chiper_words = [
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
    "y",
    "z",
]

word = input("Enter a word: ").lower()
space = int(input("Enter gap space: "))

for i in range(len(word)):
    for a in range(len(chiper_words)):
        if word[i] == chiper_words[a]:
            print(chiper_words[a + space], end="")
            break
