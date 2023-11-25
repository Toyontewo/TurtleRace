# Import the necessary modules.
import math

# Define the main function.
def main():
    # Get the user's input.
    operation = input("Enter an operation (+, -, *, /): ")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Calculate the result.
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2

    # Print the result.
    print("The result is", result)

# Call the main function.
main()