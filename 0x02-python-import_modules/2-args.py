#!/usr/bin/python
import sys

# Get the number of arguments (excluding the script name)
num_arguments = len(sys.argv) - 1

# Print the number of arguments
print("Number of argument(s):", num_arguments)

# Check if arguments were provided
if num_arguments > 0:
    print("Arguments:")
    
    # Iterate over each argument and print its position and value
    for i in range(1, num_arguments + 1):
        print("{}: {}".format(i, sys.argv[i]))
else:
    print("No arguments were passed.")
