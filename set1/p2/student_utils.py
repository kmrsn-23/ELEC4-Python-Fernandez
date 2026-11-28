# Name: Kemerson D. Fernandez
# Section: IV-BSIT-C
# Activity: P2 - Custom Module: student_utils
# Date: November 28, 2026

# Calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)


# Determine whether the student passed or failed
def determine_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Get the highest grade
def get_highest(grades):
    return max(grades)


# Get the lowest grade
def get_lowest(grades):
    return min(grades)
