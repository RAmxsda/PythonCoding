import pandas

data = pandas.read_csv("/Python 100 days challenge/Day 23/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()

output_list = {f":{letter}:{phonetic_dict[letter]} " for letter in word}
print(output_list)

save = pandas.DataFrame(output_list)
save.to_csv("output.csv")
