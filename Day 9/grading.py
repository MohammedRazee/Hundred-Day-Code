student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    grade = student_scores[key]

    if grade > 90:
        student_grades[key] = 'Outstanding'
    elif grade > 80:
        student_grades[key] = 'Exceeds Expectations'
    elif grade > 70:
        student_grades[key] = 'Acceptable'
    elif grade <= 70:
        student_grades[key] = 'Fail'

for key in student_grades:
    print(f"{key}: {student_grades[key]}")
