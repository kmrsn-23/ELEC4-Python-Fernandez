# Name: Kemerson D. Fernandez
# Section: IV-BSIT-C
# Activity: P3 - Student Record Manager
# Date: November 28, 2026

# Store student names
students = []

# Add a new student
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    # Prevent duplicate names (case-insensitive)
    for student in students:
        if student.lower() == name.lower():
            print("Student already exists!")
            return

    students.append(name)
    print(name, "has been added successfully!")

# Remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print(name, "has been removed successfully!")
            return

    print("Student not found.")

# Search for a student using a partial name
def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    if keyword == "":
        print("Search keyword cannot be empty.")
        return

    found_students = []

    for student in students:
        if keyword in student.lower():
            found_students.append(student)

    if found_students:
        print("\nSearch Results:")
        for student in found_students:
            print("-", student)
    else:
        print("No matching student found.")

# Display all students alphabetically
def display_students():
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records:")

    sorted_students = sorted(students, key=str.lower)

    for number, student in enumerate(sorted_students, start=1):
        print(number, ".", student)

    print("Total Students:", len(students))

# Main menu
def main():
    while True:
        print("\n===================================")
        print("       STUDENT RECORD MANAGER")
        print("===================================")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


# Run the program
if __name__ == "__main__":
    main()

# Difference Between List and Set:
# A list stores items in order and allows duplicate values.
# A set stores unique values and does not allow duplicates.
# In this program, a list is used to store student names.
# A set could also prevent duplicate names, but a list makes it easier to display and sort records.