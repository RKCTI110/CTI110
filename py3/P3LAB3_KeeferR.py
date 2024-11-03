# CTI 110
# P3LAB3 - Letter Grades
# KeeferR
# 11/3/24
# Convert a number grade (0 100)
# To a letter grade.


num_grade = int(input("What is the grade (0 100):"))
letter_grade = "OOPS!" # placeholder


 # ten point scale
if num_grade >= 90:
    letter_grade = "A"
elif num_grade >= 80:
    letter_grade = "B"
elif num_grade >= 70:
    letter_grade = "C"
elif num_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

    
print("Your letter grade is:", letter_grade)
