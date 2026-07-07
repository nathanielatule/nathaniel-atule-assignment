# python ro classify a studemt's grade

score1 = float(input("Enter score for Course 1: "))
score2 = float(input("Enter score for course 2: "))
score3 = float(input("Enter score fot course 3: "))
score4 = float(input("Enter score for course 4: "))
score5 = float(input("Enter score for course 5: "))

# Calculate the average score
average = (score1 + score2 + score3 + score4 + score5) /5

# Determine the grade
if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 45:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade ="F"

#Display the results
print("\n----- STUDENT RESULT -----")
print("course 1 score:", score1)
print("course 2 score:", score2)
print("course 3 score:", score3)
print("course 4 score:", score4)
print("course 5 score:", score5)
print("average score:", average)
print("Grade:", grade)

    
