# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)

# total = 0
# for temp in temp_list:
#     total += temp
# print("The average temperature: ", total/len(temp_list))
# print("The average temperature: ", data["temp"].mean())
# print(data["temp"].max())

# GET DATA IN COLUMNS
# print(data["condition"])
# print(data.condition)

# GET DATA IN ROW
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

#CREATE DATAFRAME FROM SCRATCH
data_dict ={
    "students": ["Muhammed", "Ousman", "Ali", "Ahmet"],
    "scores": [78, 85, 90, 45]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")

