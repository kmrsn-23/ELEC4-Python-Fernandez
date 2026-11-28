# Name: Kemerson D. Fernandez
# Section: IV-BSIT-C
# Activity: P4 - Safe Menu Program
# Date: November 28, 2026

# Division calculator
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    except ZeroDivisionError:
        print("Error! Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed.")

# Open and read a file
def open_file():
    filename = input("Enter filename to open: ")

    try:
        with open(filename, "r") as file:
            contents = file.read()

    except FileNotFoundError:
        print("Error! File not found.")

    else:
        print("\nFile Contents:")
        print(contents)

    finally:
        print("File operation completed.")

# Main menu
def main():
    while True:
        print("\n===================================")
        print("          SAFE MENU PROGRAM")
        print("===================================")
        print("1. Division Calculator")
        print("2. Open File")
        print("3. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you for using Safe Menu Program!")
            break

        else:
            print("Invalid menu choice! Please select 1 to 3.")


# Run the program
if __name__ == "__main__":
    main()