student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    value = student_scores[key]
    if value > 91 and value < 101:
        student_grades[key] = "Outstandin\ng"
    elif value > 81 and value < 90:
        student_grades[key] = "Exceeds Expectations\n"
    if value > 71 and value < 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

    print(key + ": " + student_grades[key])