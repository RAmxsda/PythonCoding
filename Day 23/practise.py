import pandas


numbers = [1, 2, 3, 4, 5]
new_numbers = [n + 1 for n in numbers]
add_numbers = [n * 2 for n in numbers if n % 2 == 0]
print(new_numbers)
print(add_numbers)

# List Comprehensio
name = "Angela"

letters_list = [letter.lower() for letter in name]
print(letters_list)

multiples_7 = [7 * n for n in range(1, 11)]
print(multiples_7)

sentence = "My sister name is Ankita Kumari Thapa"
# sentence_list = sentence.split()

# print(sentence_list)

# sentence_word_len = [len(length) for length in sentence_list]

# final_output = {
#     sentence_list[i]: sentence_word_len[i] for i in range(0, len(sentence_list))
# }

final_output = {word: len(word) for word in sentence.split()}
print(final_output)

weather = {
    "Sunday": 12,
    "Monday": 14,
    "Tuesday": 15,
    "Wednesday": 14,
    "Thursday": 15,
    "Friday": 21,
    "Saturday": 22,
}


"""
    While looping through dictionary
    abc = {key: value for (key, value) in dictionary.items()}
"""
weather_f = {day: f"{(temp * 9 / 5) + 32} F" for (day, temp) in weather.items()}
print(weather_f)

monthly_weather_dicttionary = {
    "january": [32, 31, 30],
    "february": [52, 31, 10],
    "march": [42, 21, 20],
    "april": [42, 31, 30],
}
weather_data_frame = pandas.DataFrame(monthly_weather_dicttionary)

print(weather_data_frame)

for index, row in weather_data_frame.iterrows():
    print(row.january)
