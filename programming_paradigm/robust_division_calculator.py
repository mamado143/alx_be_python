#!/usr/bin/python
def safe_divide(numerator, denominator):
    """Performs safe division with full error handling."""

    # 1. Convert inputs to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # 2. Try division
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
