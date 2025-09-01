from random import randint

names = ["Alex", "Razee", "Beth", "Abhilasha", "Dave", "Niggaman"]

student_scores = {n: randint(1, 100) for n in names}

print(student_scores)

passed_students = {name: score for (name, score) in student_scores.items() if score > 50}
print(passed_students)