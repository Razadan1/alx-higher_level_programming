#!/usr/bin/python3
# 100-my_calculator.py

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {'+': add, '-': sub, '*': mul, '/': div}

    operator = sys.argv[2]
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Perform the operation and store the result
    result = ops[operator](a, b)

    # Format the result to display as an integer if possible, else float
    if operator == '/' and b != 0:
        print(f"{a} {operator} {b} = {result:.1f}")  # Use float format for division
    else:
        print(f"{a} {operator} {b} = {int(result)}")  # Use integer format for other operations
