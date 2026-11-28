# Name: Kemerson D. Fernandez
# Section: IV-BSIT-C
# Activity: P2 - Custom Module: student_utils
# Date: November 28, 2026

import student_utils
from student_utils import calculate_average
from datetime import datetime


print("===================================")
print("       STUDENT GRADE REPORT")
print("===================================")

# Ask how many grades will be entered
while True:
    try:
        number_of_grades = int(input("Enter number of grades: "))

        if number_of_grades > 0:
            break
        else:
            print("Please enter a number greater than zero.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Collect the grades
grades = []

for i in range(number_of_grades):
    while True:
        try:
            grade = float(input(f"Enter grade {i + 1}: "))
            grades.append(grade)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Use the imported functions
average = calculate_average(grades)
status = student_utils.determine_status(average)
highest = student_utils.get_highest(grades)
lowest = student_utils.get_lowest(grades)

# Display the report
print("\n===================================")
print("           GRADE RESULTS")
print("===================================")

print(f"Average Grade: {average:.2f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
print(f"Status: {status}")

# Display the report generation date and time
print("\nReport Generated:")
print(datetime.now().strftime("%B %d, %Y - %I:%M %p"))

print("===================================")
