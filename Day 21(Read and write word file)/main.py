# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open(
    "/Python 100 days challenge/Day 21(Read and write word file)/Input/Names/invited_names.txt"
) as i_names:
    names = i_names.readlines()
    print(names)
with open(
    "/Python 100 days challenge/Day 21(Read and write word file)/Input/Letters/starting_letter.txt"
) as replace_letter:
    replace_letter_contents = replace_letter.read()
    for name in names:
        stripped_name = name.strip()
        output = replace_letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(
            f"/Python 100 days challenge/Day 21(Read and write word file)/Output/ReadyTOSend/letter_for_{stripped_name}.txt",
            mode="w",
        ) as completed_letter:
            completed_letter.write(output)
