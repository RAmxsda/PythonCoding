import pandas

data = pandas.read_csv("/Python 100 days challenge/Day 23/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = {f":{letter}:{phonetic_dict[letter]} " for letter in word}
    except KeyError:
        print("Only letters are allowed")
        generate_phonetic()

    else:
        print(output_list)

    save = pandas.DataFrame(output_list)
    save.to_csv("/Python 100 days challenge/Day 23/output.csv")


generate_phonetic()
