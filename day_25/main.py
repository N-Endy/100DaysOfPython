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

# data = pandas.read_csv("./weather-data.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)

# data_list = data["temp"].to_list()
# temp_avg = sum(data_list) / len(data_list)
# print(temp_avg)
# temp_avg = data["temp"].mean()
# max_temp = data["temp"].max()
# print(max_temp)

# # Get data in Rows
# row = data[data.day == "Monday"]
# print(row)

# temp_max = data[data.temp == data.temp.max()]
# print(temp_max)

# monday = data[data.day == "Monday"]
# mon_temp = int(monday.temp)
# print(mon_temp)
# temp_to_fah = (mon_temp * (9/5)) + 32
# print(temp_to_fah)

# Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angels"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("./004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

fur_color_dict = {"Fur Color": [], "Count": []}
fur_color_list = data["Primary Fur Color"].dropna().to_list()

for color in fur_color_list:
    if color in fur_color_dict["Fur Color"]:
        index = fur_color_dict["Fur Color"].index(color)
        fur_color_dict["Count"][index] += 1
    else:
        fur_color_dict["Fur Color"].append(color)
        fur_color_dict["Count"].append(1)
        
        
fur_color = pandas.DataFrame(fur_color_dict)
fur_color.to_csv("fur_color_data.csv")