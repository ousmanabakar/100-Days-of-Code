import pandas

data = pandas.read_csv("squirrel_count.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(gray_squirrels)
# print(cinnamon_squirrels)
# print(black_squirrels)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels],
    }
data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("squirrel_data.csv")

