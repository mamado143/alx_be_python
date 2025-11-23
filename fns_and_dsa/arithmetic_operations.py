#!include/usr/bin/python3
def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        return num1 + num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Can not divide by 0"
    else:
        return "Invalid operation"
