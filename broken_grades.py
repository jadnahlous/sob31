# Calculating Grades (ok, let me think about this one)

""" Write a program that will average 3 numeric exam grades, return an average test score
a corresponding letter grade, and a message stating whether the student is passing """

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))  # i deleted a ) then added in and added ()

exam_three = int(input("Input exam grade three: "))  # fixed exam3 to exam_three

grades = [exam_one, exam_two, exam_three]  # added commas for the list
sum1 = 0  # changed sum to sum1
for grade in grades:  # fixed grade to grades
    sum1 = sum1 + grade

avg = round(sum1 / len(grades))  # changed grdes to grades and added round to it can round up the values

if avg >= 90:
    letter_grade = "A"
elif 80 <= avg < 90:  # i added : and made avg range between 80 and 90
    letter_grade = "B"
elif 69 < avg < 80:  # made avg range between 69 and 80
    letter_grade = "C"  # added "
elif 69 >= avg >= 65:
    letter_grade = "D"
else:  # changed elif to else
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))  # added a backspace
print("Grade: " + letter_grade)

if letter_grade == "F":  # removed - and replaced it with "_"
    print("Student is failing.")  # added ()
else:
    print("Student is passing.")  # added ()
