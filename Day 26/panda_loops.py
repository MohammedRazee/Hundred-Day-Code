import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

student_data = pd.DataFrame(student_dict)
# print(student_data)

# Looping through rows of a data frame
for(index, row) in student_data.iterrows():
    if row.student == "Angela":
        print(row.score)
