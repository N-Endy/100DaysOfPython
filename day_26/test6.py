student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# # Loop through Data Frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows for a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)