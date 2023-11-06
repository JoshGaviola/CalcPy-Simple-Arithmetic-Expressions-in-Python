num1 = 0.0
num2 = 0.0
operator = ""
result = 0.0

num1 = float(input("Enter the first number: "))

operator = input("Choose an operator (+ for addition, - for subtraction, * for multiplication, / for division): ")

num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operator. Please choose +, -, *, or /.")

print("Result: ", result)
