import numpy as np

def add_numbers(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract_numbers(a, b):
    """Return the difference between a and b."""
    return a - b

def multiply_numbers(a, b):
    """Return the product of a and b."""
    return a * b

def divide_numbers(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    # Static values
    x = 600
    y = 20000

    print("Simple Calculator with Static Values\n")

    print(f"Adding {x} and {y}: {x} + {y} = {add_numbers(x, y)}")
    print(f"Subtracting {y} from {x}: {x} - {y} = {subtract_numbers(x, y)}")
    print(f"Multiplying {x} and {y}: {x} * {y} = {multiply_numbers(x, y)}")
    print(f"Dividing {x} by {y}: {x} / {y} = {divide_numbers(x, y)}")
