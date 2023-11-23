# data = []
# with open("./weather-data.csv") as weather_data:
#     raw_data = weather_data.readlines()
#     for _ in raw_data:
#         data.append(_.strip())
#     print(data)

# import csv
# with open("./weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp": # if row[1] != "temp"
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather-data.csv")
# print(data["temp"])
data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
# temp_avg = sum(data_list) / len(data_list)
# print(temp_avg)
temp_avg = data["temp"].mean()
max_temp = data["temp"].max()
print(max_temp)
