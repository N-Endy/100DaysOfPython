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
print(data["temp"])