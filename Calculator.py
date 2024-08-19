# Simple Command-Line Calculator in Python

def show_menu():
    print("\nSimple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_calculation(choice, num1, num2):
    if choice == '1':
        return num1 + num2
    elif choice == '2':
        return num1 - num2
    elif choice == '3':
        return num1 * num2
    elif choice == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation."

def main():
    while True:
        show_menu()
        choice = input("Choose an operation: ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        result = perform_calculation(choice, num1, num2)
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()
