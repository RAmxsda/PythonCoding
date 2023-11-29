# import csv

# with open("/Python 100 days challenge/Day 22(pandas)/weather_data.csv") as data_weather:
#     data = csv.reader(data_weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

pandas.read_csv("/Python 100 days challenge/Day 22(pandas)/weather_data.csv")

data = pandas.read_csv("/Python 100 days challenge/Day 22(pandas)/weather_data.csv")


print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

data_temp = data["temp"].to_list()

print(data_temp)

print(data["temp"].mean())

print(data["temp"].max())

print(data["condition"])

print(data.condition)

monday = data[data.day == "Monday"]

print(monday.condition)

monday_temp = int(monday.temp)

monday_temp_f = monday_temp * 9 / 5 + 32

print(monday_temp_f)


# Create a dataframe from scratch

data_dict = {
    "students": ["RAM", "HARI", "GANGATAULE"],
    "subject": ["Math", "Science", "History"],
    "scores": [76, 56, 65],
}


data = pandas.DataFrame(data_dict)

data.to_csv("new_data.csv")
