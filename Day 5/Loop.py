# For loop to calculate the height of students

student_heights = input("enter hieghts").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0;

for height in student_heights:
    total_height += height;
print("Total height is " + str(total_height));

number_of_students = 0;
for student in student_heights:
    number_of_students += 1;

average_height = round(total_height / number_of_students);
print("Average height of Anaconda damna is  " + str(average_height))


