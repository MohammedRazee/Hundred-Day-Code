# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Charoline", "Dave", "Elanor", "Freddie"]
student_scores = {
    key: random.randint(1, 100) for key in names
}
# print(student_scores)

passed_students = {
    student:scores for (student, scores) in student_scores.items() if scores > 50
}
print(passed_students)
