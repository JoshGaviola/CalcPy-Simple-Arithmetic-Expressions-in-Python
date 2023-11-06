def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator_input():
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Choose an operator (+, -, *, /): ")
        if operator in valid_operators:
            return operator
        else:
            print("Invalid operator. Please choose +, -, *, or /.")

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return num1 / num2

while True:
    try:
        print("Calculator:")
        
        num1 = get_number_input("Enter the first number: ")
        operator = get_operator_input()
        num2 = get_number_input("Enter the second number: ")
        result = calculate(num1, operator, num2)
        print("Result:", result)
    except ZeroDivisionError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nCalculation aborted.")
    except Exception as e:
        print(f"An error occurred: {e}")

    exit_command = input("Enter 'exit' to end the program, or press Enter to continue: ")
    if exit_command.lower() == "exit":
        break
