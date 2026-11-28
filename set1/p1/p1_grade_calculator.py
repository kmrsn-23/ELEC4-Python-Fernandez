
# Name: Kemerson D. Fernandez
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator
# Date: November 23, 2026

# Function 1: Accept student grades
def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("How many grades? "))
            if count <= 0:
                print("Please enter at least 1 grade.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be from 0 to 100.")

            except ValueError:
                print("Invalid input. Enter a number.")

    return grades

# Function 2: Calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function 3: Get highest grade
def get_highest(grades):
    return max(grades)

# Function 4: Get lowest grade
def get_lowest(grades):
    return min(grades)

# Function 5: Determine pass or fail
def get_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Main menu of the program
def main():
    grades = []

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("Name: Kemerson D. Fernandez")
        print("Section: IV-BSIT-C")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            grades = enter_grades()
            print("Grades saved successfully!")

        elif choice == "2":
            if not grades:
                print("Please enter grades first.")
            else:
                print("\n===== GRADE RESULTS =====")
                print(f"Average: {calculate_average(grades):.2f}")
                print(f"Highest Grade: {get_highest(grades):.2f}")
                print(f"Lowest Grade: {get_lowest(grades):.2f}")
                print(f"Status: {get_status(grades)}")

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()


# Local variables are created inside a function.
# In my program, grades inside main() is a local variable.
# A global variable is created outside functions and can be
# accessed by different functions in the same file.
# I used local variables to keep my program organized.

