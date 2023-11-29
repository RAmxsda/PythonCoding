import pandas

data = pandas.read_csv(
    "/Python 100 days challenge/Day 22(pandas)/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv"
)


gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])


red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(data[data["Primary Fur Color"].notnull()])
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)

df.to_csv("/Python 100 days challenge/Day 22(pandas)/squirrel_count.csv")

print(df)
