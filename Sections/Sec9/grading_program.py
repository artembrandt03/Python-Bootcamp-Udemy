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
for name in student_scores:
  if student_scores[name] <= 70:
    student_grades[name] = "Fail"
  elif 71 <= student_scores[name] <= 80:
    student_grades[name] = "Acceptable"
  elif 81 <= student_scores[name] <= 90:
    student_grades[name] = "Exceeds Expectations"
  elif student_scores[name] >= 91:
    student_grades[name] = "Outstanding"

#teacher's solution for todo 2:
#for score in student_scores:
    #score = student_scores[student]
    #if score = 90:
    #...
#this is a more efficient solution

# 🚨 Don't change the code below 👇
print(student_grades)