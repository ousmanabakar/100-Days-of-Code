import random

names = ["Ousman", "Ali", "Martin", "Malcolm", "Baldwin", "Haroun"]
students_scores = {name: random.randint(30, 100) for name in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 50}
print(passed_students)



