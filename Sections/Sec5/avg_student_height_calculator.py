# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total_height = 0
num_of_students = 0

for height in student_heights:
    total_height += height
    num_of_students += 1

avg_height = round(total_height/num_of_students)
print(avg_height)
input("Press anything to exit the program.\n")

#the challenge was not to use sum() and len() functions, but if i could the solution would be like this:
#total_height = sum(student_heights)
#num_of_students = len(student_heights)
#avg_height = round(total_height/num_of_students)

#solution comparing to the teacher: she split the for loop in 2, for total height and num of students. 
#mine is basically more efficient 